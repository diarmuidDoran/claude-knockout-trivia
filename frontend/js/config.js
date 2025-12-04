// Configuration for the Knockout Trivia game
// Automatically detect if we're accessing from a different device
const isLocalhost = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';
const backendHost = isLocalhost ? 'localhost' : window.location.hostname;

// Detect if running via nginx (Docker mode) or direct development
const currentPort = window.location.port;
const isDockerMode = currentPort === '' || currentPort === '80'; // Removed 3000 - that's our dev server!

// In Docker mode, use relative URLs (nginx proxies to backend)
// In development mode, connect directly to backend on port 8001 (or 8000)
const API_BASE = isDockerMode ? '' : `http://${backendHost}:8001`;
const WS_PROTOCOL = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
const WS_BASE = isDockerMode ? `${WS_PROTOCOL}//${window.location.host}` : `ws://${backendHost}:8001`;

const CONFIG = {
    // API Configuration
    API_BASE_URL: API_BASE,
    API_URL: `${API_BASE}/api`,
    WS_BASE_URL: WS_BASE,
    
    // Game Settings
    QUESTION_TIME_LIMIT: 30, // seconds
    MAX_PLAYERS_PER_ROOM: 10,
    
    // UI Settings
    ANIMATION_DURATION: 300, // milliseconds
    NOTIFICATION_DURATION: 3000, // milliseconds
    TIMER_WARNING_THRESHOLD: 10, // seconds
    TIMER_DANGER_THRESHOLD: 5, // seconds
    
    // Reconnection Settings
    RECONNECT_ATTEMPTS: 5,
    RECONNECT_DELAY: 2000, // milliseconds
    
    // Endpoints
    ENDPOINTS: {
        CREATE_ROOM: '/api/rooms/create',
        JOIN_ROOM: '/api/rooms/join',
        GET_ROOM: '/api/rooms',
        GET_PLAYERS: '/api/rooms/{roomCode}/players',
        SUBMIT_ANSWER: '/api/game/{roomCode}/submit-answer',
        GET_CURRENT_QUESTION: '/api/game/{roomCode}/current-question',
        GET_LEADERBOARD: '/api/game/{roomCode}/leaderboard',
        START_GAME: '/api/game/start',
        WEBSOCKET: '/ws/{roomCode}/{playerId}'
    },
    
    // Game States
    GAME_STATES: {
        WAITING: 'waiting',
        STARTING: 'starting', 
        ACTIVE: 'active',
        FINISHED: 'finished'
    },
    
    // WebSocket Message Types
    WS_MESSAGE_TYPES: {
        PING: 'ping',
        PONG: 'pong',
        PLAYER_JOINED: 'player_joined',
        PLAYER_LEFT: 'player_left',
        PLAYER_DISCONNECTED: 'player_disconnected',
        PLAYER_ANSWERED: 'player_answered',
        PLAYER_READY: 'player_ready',
        NEW_QUESTION: 'new_question',
        QUESTION_RESULTS: 'question_results',
        GAME_STARTED: 'game_started',
        GAME_ENDED: 'game_ended',
        ERROR: 'error'
    },
    
    // Screen IDs
    SCREENS: {
        LOADING: 'loading-screen',
        JOIN: 'join-screen',
        WAITING: 'waiting-screen',
        GAME: 'game-screen',
        LEADERBOARD: 'leaderboard-screen'
    }
};

// Utility functions
const Utils = {
    // Format time as MM:SS or SS
    formatTime: (seconds) => {
        if (seconds >= 60) {
            const mins = Math.floor(seconds / 60);
            const secs = seconds % 60;
            return `${mins}:${secs.toString().padStart(2, '0')}`;
        }
        return seconds.toString();
    },
    
    // Format score with commas
    formatScore: (score) => {
        return score.toLocaleString();
    },
    
    // Capitalize first letter
    capitalize: (str) => {
        return str.charAt(0).toUpperCase() + str.slice(1);
    },
    
    // Generate random ID
    generateId: () => {
        return Math.random().toString(36).substr(2, 9);
    },
    
    // Validate room code format
    isValidRoomCode: (code) => {
        return /^[A-Z]{6}$/.test(code);
    },
    
    // Validate player name
    isValidPlayerName: (name) => {
        return name && name.trim().length >= 2 && name.trim().length <= 20;
    },
    
    // Debounce function
    debounce: (func, wait) => {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },
    
    // Get emoji for rank
    getRankEmoji: (rank) => {
        switch (rank) {
            case 1: return '🥇';
            case 2: return '🥈'; 
            case 3: return '🥉';
            default: return '🏅';
        }
    },
    
    // Play sound effect (if available)
    playSound: (type) => {
        // In a full implementation, you'd have actual sound files
        switch (type) {
            case 'correct':
                // Play correct answer sound
                break;
            case 'incorrect':
                // Play incorrect answer sound
                break;
            case 'tick':
                // Play timer tick sound
                break;
            case 'notification':
                // Play notification sound
                break;
        }
    },
    
    // Vibrate device (if supported)
    vibrate: (pattern = [100]) => {
        if ('vibrate' in navigator) {
            navigator.vibrate(pattern);
        }
    }
};

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { CONFIG, Utils };
}