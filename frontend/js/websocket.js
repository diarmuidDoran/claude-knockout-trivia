// WebSocket Manager for real-time communication
class WebSocketManager {
    constructor() {
        this.ws = null;
        this.roomCode = null;
        this.playerId = null;
        this.reconnectAttempts = 0;
        this.isConnected = false;
        this.messageQueue = [];
        this.eventListeners = {};
        this.heartbeatInterval = null;
        
        // Bind methods
        this.connect = this.connect.bind(this);
        this.disconnect = this.disconnect.bind(this);
        this.send = this.send.bind(this);
        this.onMessage = this.onMessage.bind(this);
        this.onOpen = this.onOpen.bind(this);
        this.onClose = this.onClose.bind(this);
        this.onError = this.onError.bind(this);
    }
    
    // Connect to WebSocket
    connect(roomCode, playerId) {
        this.roomCode = roomCode;
        this.playerId = playerId;
        
        const wsUrl = `${CONFIG.WS_BASE_URL}${CONFIG.ENDPOINTS.WEBSOCKET
            .replace('{roomCode}', roomCode)
            .replace('{playerId}', playerId)}`;
            
        console.log('Connecting to WebSocket:', wsUrl);
        
        try {
            this.ws = new WebSocket(wsUrl);
            this.ws.onopen = this.onOpen;
            this.ws.onmessage = this.onMessage;
            this.ws.onclose = this.onClose;
            this.ws.onerror = this.onError;
            
            this.updateConnectionStatus('connecting');
        } catch (error) {
            console.error('WebSocket connection error:', error);
            this.handleConnectionError();
        }
    }
    
    // Disconnect from WebSocket
    disconnect() {
        this.isConnected = false;
        
        if (this.heartbeatInterval) {
            clearInterval(this.heartbeatInterval);
            this.heartbeatInterval = null;
        }
        
        if (this.ws) {
            this.ws.close(1000, 'Normal closure');
            this.ws = null;
        }
        
        this.updateConnectionStatus('disconnected');
    }
    
    // Handle WebSocket open
    onOpen(event) {
        console.log('WebSocket connected');
        this.isConnected = true;
        this.reconnectAttempts = 0;
        this.updateConnectionStatus('connected');
        
        // Send queued messages
        while (this.messageQueue.length > 0) {
            const message = this.messageQueue.shift();
            this.send(message);
        }
        
        // Start heartbeat
        this.startHeartbeat();
        
        // Emit connected event
        this.emit('connected');
    }
    
    // Handle WebSocket message
    onMessage(event) {
        try {
            const data = JSON.parse(event.data);
            console.log('WebSocket message received:', data);
            
            // Handle pong response
            if (data.type === CONFIG.WS_MESSAGE_TYPES.PONG) {
                return;
            }
            
            // Emit message event
            this.emit('message', data);
            this.emit(data.type, data);
            
        } catch (error) {
            console.error('Error parsing WebSocket message:', error);
        }
    }
    
    // Handle WebSocket close
    onClose(event) {
        console.log('WebSocket closed:', event.code, event.reason);
        this.isConnected = false;
        
        if (this.heartbeatInterval) {
            clearInterval(this.heartbeatInterval);
            this.heartbeatInterval = null;
        }
        
        this.updateConnectionStatus('disconnected');
        this.emit('disconnected', { code: event.code, reason: event.reason });
        
        // Attempt reconnection if not a normal closure
        if (event.code !== 1000 && this.reconnectAttempts < CONFIG.RECONNECT_ATTEMPTS) {
            this.attemptReconnect();
        }
    }
    
    // Handle WebSocket error
    onError(error) {
        console.error('WebSocket error:', error);
        this.emit('error', error);
        this.handleConnectionError();
    }
    
    // Send message through WebSocket
    send(message) {
        if (this.isConnected && this.ws && this.ws.readyState === WebSocket.OPEN) {
            const messageStr = typeof message === 'string' ? message : JSON.stringify(message);
            this.ws.send(messageStr);
            console.log('WebSocket message sent:', messageStr);
        } else {
            // Queue message for later
            this.messageQueue.push(message);
            console.log('Message queued (not connected):', message);
        }
    }
    
    // Attempt to reconnect
    attemptReconnect() {
        if (this.reconnectAttempts >= CONFIG.RECONNECT_ATTEMPTS) {
            console.log('Max reconnection attempts reached');
            this.emit('reconnect_failed');
            return;
        }
        
        this.reconnectAttempts++;
        this.updateConnectionStatus('connecting');
        
        console.log(`Attempting to reconnect (${this.reconnectAttempts}/${CONFIG.RECONNECT_ATTEMPTS})`);
        
        setTimeout(() => {
            if (this.roomCode && this.playerId) {
                this.connect(this.roomCode, this.playerId);
            }
        }, CONFIG.RECONNECT_DELAY);
    }
    
    // Start heartbeat to keep connection alive
    startHeartbeat() {
        this.heartbeatInterval = setInterval(() => {
            if (this.isConnected) {
                this.send({ type: CONFIG.WS_MESSAGE_TYPES.PING });
            }
        }, 30000); // Ping every 30 seconds
    }
    
    // Handle connection errors
    handleConnectionError() {
        this.updateConnectionStatus('error');
        
        // Show user-friendly error message
        if (typeof window !== 'undefined' && window.UI) {
            window.UI.showNotification('Connection lost. Trying to reconnect...', 'error');
        }
    }
    
    // Update connection status in UI
    updateConnectionStatus(status) {
        const statusElement = document.getElementById('connection-status');
        const statusText = document.querySelector('.status-text');
        
        if (!statusElement || !statusText) return;
        
        statusElement.className = `connection-status ${status}`;
        
        switch (status) {
            case 'connected':
                statusText.textContent = 'Connected';
                statusElement.classList.add('hidden');
                break;
            case 'connecting':
                statusText.textContent = 'Connecting...';
                statusElement.classList.remove('hidden');
                break;
            case 'disconnected':
                statusText.textContent = 'Disconnected';
                statusElement.classList.remove('hidden');
                break;
            case 'error':
                statusText.textContent = 'Connection Error';
                statusElement.classList.remove('hidden');
                break;
        }
    }
    
    // Event system
    on(eventType, callback) {
        if (!this.eventListeners[eventType]) {
            this.eventListeners[eventType] = [];
        }
        this.eventListeners[eventType].push(callback);
    }
    
    off(eventType, callback) {
        if (this.eventListeners[eventType]) {
            const index = this.eventListeners[eventType].indexOf(callback);
            if (index > -1) {
                this.eventListeners[eventType].splice(index, 1);
            }
        }
    }
    
    emit(eventType, data) {
        if (this.eventListeners[eventType]) {
            this.eventListeners[eventType].forEach(callback => {
                try {
                    callback(data);
                } catch (error) {
                    console.error('Error in event listener:', error);
                }
            });
        }
    }
    
    // Send ready signal
    sendReady() {
        this.send({ type: CONFIG.WS_MESSAGE_TYPES.PLAYER_READY });
    }
    
    // Send answer submitted notification
    sendAnswerSubmitted(questionId, selectedOptionId) {
        this.send({
            type: CONFIG.WS_MESSAGE_TYPES.ANSWER_SUBMITTED,
            questionId,
            selectedOptionId
        });
    }
    
    // Get connection status
    getConnectionStatus() {
        return {
            isConnected: this.isConnected,
            reconnectAttempts: this.reconnectAttempts,
            roomCode: this.roomCode,
            playerId: this.playerId
        };
    }

    // Alias for connect to support different naming conventions
    joinRoom(roomCode, playerId) {
        return this.connect(roomCode, playerId);
    }
}

// Export WebSocketManager
if (typeof window !== 'undefined') {
    window.WebSocketManager = WebSocketManager;
}