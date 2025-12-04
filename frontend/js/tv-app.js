// TV App - Main controller for laptop/TV screen
class TVApp {
    constructor() {
        this.wsManager = null;
        this.hostPlayerId = null;
        this.pollingInterval = null;
        this.timerInterval = null; // Store timer interval to clear it when needed
        this.autoReturnTimeout = null; // Auto-return to home screen timer
        this.hauntingRaceManager = null;
        this.gameState = {
            roomCode: null,
            players: [],
            currentQuestion: null,
            questionNumber: 0,
            gameStatus: 'home' // 'home', 'waiting', 'playing', 'results'
        };

        this.init();
    }

    // Initialize TV application
    init() {
        console.log('Initializing TV App');

        // Setup WebSocket
        this.wsManager = new WebSocketManager();
        this.setupWebSocketListeners();

        // Setup UI event listeners
        this.setupUIListeners();

        // Load leaderboard
        this.loadLeaderboard();

        // Check for existing TV session and restore if found
        this.restoreTVSession();

        console.log('TV App initialized');
    }

    // Setup WebSocket event listeners
    setupWebSocketListeners() {
        this.wsManager.on('connected', () => {
            console.log('TV WebSocket connected');
        });

        this.wsManager.on('disconnected', () => {
            console.log('TV WebSocket disconnected');
        });

        this.wsManager.on('room_created', (data) => {
            console.log('Room created:', data);
            this.handleRoomCreated(data);
        });

        this.wsManager.on('player_joined', (data) => {
            console.log('Player joined:', data);
            this.handlePlayerJoined(data);
        });

        this.wsManager.on('player_left', (data) => {
            console.log('Player left:', data);
            this.handlePlayerLeft(data);
        });

        this.wsManager.on('game_started', (data) => {
            console.log('Game started:', data);
            this.handleGameStarted(data);
        });

        // Only listen for 'new_question' - removed duplicate 'question' listener to prevent double handling
        this.wsManager.on('new_question', (data) => {
            console.log('New question:', data);
            this.handleNewQuestion(data);
        });

        this.wsManager.on('player_answered', (data) => {
            console.log('Player answered:', data);
            this.handlePlayerAnswered(data);
        });

        this.wsManager.on('question_results', (data) => {
            console.log('Question results:', data);
            this.handleQuestionResults(data);
        });

        this.wsManager.on('game_ended', (data) => {
            console.log('Game ended:', data);
            this.handleGameEnded(data);
        });

        this.wsManager.on('rematch_started', (data) => {
            console.log('Rematch started:', data);
            this.handleRematchStarted(data);
        });

        this.wsManager.on('game_finished', (data) => {
            console.log('Game finished:', data);
            this.handleGameFinished(data);
        });

        this.wsManager.on('start_timer', (data) => {
            console.log('Start timer signal received:', data);
            this.handleStartTimer(data);
        });

        // Mini-game event handlers
        this.wsManager.on('mini_game_start', (data) => {
            console.log('Mini-game started:', data);
            this.handleMiniGameStart(data);
        });

        this.wsManager.on('mini_game_player_action', (data) => {
            console.log('Mini-game player action:', data);
            this.handleMiniGamePlayerAction(data);
        });

        this.wsManager.on('mini_game_results', (data) => {
            console.log('Mini-game results:', data);
            this.handleMiniGameResults(data);
        });

        this.wsManager.on('mini_game_timeout', (data) => {
            console.log('Mini-game timeout:', data);
            this.handleMiniGameTimeout(data);
        });

        this.wsManager.on('mini_game_phase_change', (data) => {
            console.log('Mini-game phase change:', data);
            this.handleMiniGamePhaseChange(data);
        });
    }

    // Setup UI event listeners
    setupUIListeners() {
        const startGameBtn = document.getElementById('start-new-game-btn');
        if (startGameBtn) {
            startGameBtn.addEventListener('click', () => {
                this.createNewRoom();
            });
        }

        const exitRoomBtn = document.getElementById('exit-room-btn');
        if (exitRoomBtn) {
            exitRoomBtn.addEventListener('click', () => {
                this.handleExitRoom();
            });
        }

        const rematchBtn = document.getElementById('rematch-btn');
        if (rematchBtn) {
            rematchBtn.addEventListener('click', () => {
                this.handleRematch();
            });
        }

        const finishBtn = document.getElementById('finish-game-btn');
        if (finishBtn) {
            finishBtn.addEventListener('click', () => {
                this.handleFinishGame();
            });
        }

        const resetLeaderboardBtn = document.getElementById('reset-leaderboard-btn');
        if (resetLeaderboardBtn) {
            resetLeaderboardBtn.addEventListener('click', () => {
                this.handleResetLeaderboard();
            });
        }

        const emergencyTerminateBtn = document.getElementById('emergency-terminate-btn');
        if (emergencyTerminateBtn) {
            emergencyTerminateBtn.addEventListener('click', () => {
                this.handleEmergencyTerminate();
            });
        }

        const gameOverTerminateBtn = document.getElementById('game-over-terminate-btn');
        if (gameOverTerminateBtn) {
            gameOverTerminateBtn.addEventListener('click', () => {
                this.handleEmergencyTerminate();
            });
        }

        const hauntingRaceTerminateBtn = document.getElementById('haunting-race-terminate-btn');
        if (hauntingRaceTerminateBtn) {
            hauntingRaceTerminateBtn.addEventListener('click', () => {
                this.handleEmergencyTerminate();
            });
        }
    }

    // Create new game room
    async createNewRoom() {
        try {
            // Check if there's already an active room for this TV
            const existingRoomCode = localStorage.getItem('tv_room_code');
            if (existingRoomCode) {
                console.log('[TV SESSION] Found existing room code:', existingRoomCode);

                // Check if the room still exists
                const checkResponse = await fetch(`${CONFIG.API_BASE_URL}/api/rooms/${existingRoomCode}`);
                if (checkResponse.ok) {
                    const roomData = await checkResponse.json();
                    if (roomData.is_active) {
                        alert('This TV already has an active game room. Please finish or complete the current game first.');
                        // Restore to the existing room
                        await this.restoreTVSession();
                        return;
                    }
                }

                // If room doesn't exist or isn't active, clear the saved code
                localStorage.removeItem('tv_room_code');
            }

            console.log('Creating new game room...');

            const response = await fetch(`${CONFIG.API_BASE_URL}/api/rooms/create`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    host_name: 'TV_HOST'
                })
            });

            if (response.ok) {
                const data = await response.json();
                console.log('Room created successfully:', data);

                this.gameState.roomCode = data.room_code || data.code;

                // Save room code to localStorage for session persistence
                localStorage.setItem('tv_room_code', this.gameState.roomCode);
                console.log('[TV SESSION] Saved room code to localStorage:', this.gameState.roomCode);
                console.log('[TV SESSION] Verification - localStorage now contains:', localStorage.getItem('tv_room_code'));

                // No host player anymore - initialize empty
                this.gameState.players = [];

                // Connect TV to WebSocket for game events (use 'tv' as player_id for TV)
                console.log('TV connecting to WebSocket...');
                this.wsManager.connect(this.gameState.roomCode, 'tv');

                // Initialize Haunting Race Manager for TV
                this.hauntingRaceManager = new HauntingRaceManager(this.wsManager, 'tv', true);

                // Switch to waiting screen
                this.showWaitingScreen(this.gameState.roomCode);

                // Poll for player updates every 2 seconds
                this.startPlayerPolling();
            } else {
                const errorData = await response.json();
                console.error('Error creating room:', errorData);
                alert('Failed to create room. Please try again.');
            }
        } catch (error) {
            console.error('Error creating room:', error);
            alert('Failed to create room. Please check your connection.');
        }
    }

    // Restore TV session on page load
    async restoreTVSession() {
        const savedRoomCode = localStorage.getItem('tv_room_code');

        console.log('[TV SESSION] Checking for saved session...');
        console.log('[TV SESSION] localStorage tv_room_code:', savedRoomCode);

        if (!savedRoomCode) {
            console.log('[TV SESSION] No saved room code found - staying on home screen');
            return;
        }

        console.log('[TV SESSION] Found saved room code:', savedRoomCode);

        try {
            // Query backend for room status
            const response = await fetch(`${CONFIG.API_BASE_URL}/api/rooms/${savedRoomCode}`);

            if (!response.ok) {
                console.log('[TV SESSION] Room no longer exists, clearing saved session');
                localStorage.removeItem('tv_room_code');
                return;
            }

            const roomData = await response.json();
            console.log('[TV SESSION] Room data:', roomData);

            // Check if room is still active
            if (!roomData.is_active) {
                console.log('[TV SESSION] Room is no longer active, clearing saved session');
                localStorage.removeItem('tv_room_code');
                return;
            }

            // Restore room state
            this.gameState.roomCode = savedRoomCode;

            // Connect to WebSocket
            console.log('[TV SESSION] Reconnecting to WebSocket...');
            this.wsManager.connect(savedRoomCode, 'tv');

            // Initialize Haunting Race Manager for TV
            this.hauntingRaceManager = new HauntingRaceManager(this.wsManager, 'tv', true);

            // Get players in room
            const playersResponse = await fetch(`${CONFIG.API_BASE_URL}/api/rooms/${savedRoomCode}/players`);
            if (playersResponse.ok) {
                const players = await playersResponse.json();
                this.gameState.players = players;
                console.log('[TV SESSION] Loaded players:', players);
            }

            // Show appropriate screen based on game state
            const gameState = roomData.game_state.toUpperCase();
            console.log('[TV SESSION] Game state (raw):', roomData.game_state);
            console.log('[TV SESSION] Game state (uppercase):', gameState);
            console.log('[TV SESSION] Checking conditions - WAITING?', gameState === 'WAITING', 'ACTIVE?', gameState === 'ACTIVE', 'STARTING?', gameState === 'STARTING', 'FINISHED?', gameState === 'FINISHED');

            if (gameState === 'WAITING') {
                console.log('[TV SESSION] ✓ Condition met: WAITING - Restoring to waiting screen');
                this.showWaitingScreen(savedRoomCode);
                this.updatePlayersDisplay();
                this.startPlayerPolling();
            } else if (gameState === 'ACTIVE' || gameState === 'STARTING') {
                console.log('[TV SESSION] ✓ Condition met: ACTIVE/STARTING - Restoring to game screen');
                this.showGameScreen();
                this.updatePlayersDisplay();
                this.startPlayerPolling();

                // If there's a current question, we'll get it via WebSocket
            } else if (gameState === 'FINISHED') {
                console.log('[TV SESSION] ✓ Condition met: FINISHED - Showing game over screen');
                // Fetch player data to show as final leaderboard
                const playersForLeaderboard = this.gameState.players || [];
                if (playersForLeaderboard.length > 0) {
                    // Sort by score descending
                    playersForLeaderboard.sort((a, b) => (b.total_score || 0) - (a.total_score || 0));

                    // Create leaderboard data in the expected format
                    const leaderboardData = {
                        final_leaderboard: playersForLeaderboard.map((player, index) => ({
                            rank: index + 1,
                            player_id: player.id,
                            player_name: player.name,
                            total_score: player.total_score || 0,
                            is_ghost: player.is_ghost || false
                        }))
                    };
                    this.handleGameEnded(leaderboardData);
                } else {
                    // No player data available, just show the screen
                    this.showGameOverScreen();
                }
            } else {
                console.log('[TV SESSION] ✗ No condition met! Unexpected game state:', gameState);
            }

            console.log('[TV SESSION] Session restored successfully');

        } catch (error) {
            console.error('[TV SESSION] Error restoring session:', error);
            localStorage.removeItem('tv_room_code');
        }
    }

    // Show waiting screen
    showWaitingScreen(roomCode) {
        // Hide home screen
        document.getElementById('tv-home-screen').classList.add('hidden');

        // Show waiting screen
        const waitingScreen = document.getElementById('tv-waiting-screen');
        waitingScreen.classList.remove('hidden');

        // Display room code
        document.getElementById('tv-room-code').textContent = roomCode;

        // Update game status
        this.gameState.gameStatus = 'waiting';
        this.updateWaitingMessage();

        console.log(`Waiting screen shown for room: ${roomCode}`);
    }

    // Show game screen
    showGameScreen() {
        // Hide all other screens
        document.getElementById('tv-home-screen').classList.add('hidden');
        document.getElementById('tv-waiting-screen').classList.add('hidden');
        document.getElementById('tv-game-over-screen').classList.add('hidden');
        const hauntingRaceScreen = document.getElementById('haunting-race-screen');
        if (hauntingRaceScreen) {
            hauntingRaceScreen.classList.add('hidden');
        }

        // Show game screen
        const gameScreen = document.getElementById('tv-game-screen');
        gameScreen.classList.remove('hidden');

        this.gameState.gameStatus = 'playing';
        console.log('Game screen shown');
    }

    // Show game over screen
    showGameOverScreen() {
        // Hide all other screens
        document.getElementById('tv-home-screen').classList.add('hidden');
        document.getElementById('tv-waiting-screen').classList.add('hidden');
        document.getElementById('tv-game-screen').classList.add('hidden');

        // Show game over screen
        const gameOverScreen = document.getElementById('tv-game-over-screen');
        gameOverScreen.classList.remove('hidden');

        this.gameState.gameStatus = 'finished';
        console.log('Game over screen shown');
    }

    // Handle exit room button click
    async handleExitRoom() {
        if (!this.gameState.roomCode) {
            console.error('No active room to exit');
            return;
        }

        // Confirm the user wants to exit
        const confirmExit = confirm('Are you sure you want to exit and delete this room? All players will be disconnected.');
        if (!confirmExit) {
            return;
        }

        try {
            console.log('[EXIT ROOM] Exiting room:', this.gameState.roomCode);

            // Stop player polling
            this.stopPlayerPolling();

            // Disconnect WebSocket
            if (this.wsManager) {
                this.wsManager.disconnect();
            }

            // Delete the room via API
            const response = await fetch(`${CONFIG.API_BASE_URL}/api/rooms/${this.gameState.roomCode}`, {
                method: 'DELETE'
            });

            if (response.ok) {
                console.log('[EXIT ROOM] Room deleted successfully');
            } else {
                console.error('[EXIT ROOM] Failed to delete room');
            }

            // Clear saved room code from localStorage
            localStorage.removeItem('tv_room_code');
            console.log('[EXIT ROOM] Cleared saved room code');

            // Reset game state
            this.gameState = {
                roomCode: null,
                players: [],
                currentQuestion: null,
                questionNumber: 0,
                gameStatus: 'home'
            };

            // Return to home screen
            document.querySelectorAll('.screen').forEach(screen => {
                screen.classList.add('hidden');
            });
            document.getElementById('tv-home-screen').classList.remove('hidden');

            // Reload leaderboard
            this.loadLeaderboard();

            console.log('[EXIT ROOM] Returned to home screen');

        } catch (error) {
            console.error('[EXIT ROOM] Error exiting room:', error);
            alert('Failed to exit room. Please try again.');
        }
    }

    // Handle room created event
    handleRoomCreated(data) {
        console.log('Room created event received:', data);
        // Room creation is handled in createNewRoom
    }

    // Handle player joined event
    handlePlayerJoined(data) {
        console.log('Player joined event:', data);
        
        // Add player to local state
        const existingPlayerIndex = this.gameState.players.findIndex(p => p.id === data.player.id);
        if (existingPlayerIndex === -1) {
            this.gameState.players.push(data.player);
        } else {
            this.gameState.players[existingPlayerIndex] = data.player;
        }
        
        // Update TV display
        this.updatePlayersDisplay();
        this.updateWaitingMessage();
    }

    // Handle player left event
    handlePlayerLeft(data) {
        console.log('Player left event:', data);
        
        // Remove player from local state
        this.gameState.players = this.gameState.players.filter(p => p.id !== data.player_id);
        
        // Update TV display
        this.updatePlayersDisplay();
        this.updateWaitingMessage();
    }

    // Update players display on TV
    updatePlayersDisplay() {
        const playersContainer = document.getElementById('tv-players-list');
        const playerCountElement = document.getElementById('player-count');
        
        if (!playersContainer || !playerCountElement) return;

        // Filter out TV host
        const realPlayers = this.gameState.players.filter(p => p.name !== 'TV_HOST');
        
        // Update player count
        playerCountElement.textContent = realPlayers.length;
        
        // Clear current players
        playersContainer.innerHTML = '';
        
        // Add players
        realPlayers.forEach(player => {
            const playerCard = document.createElement('div');
            playerCard.className = 'player-card';
            if (player.is_vip) {
                playerCard.classList.add('vip');
            }
            
            playerCard.innerHTML = `
                <div class="player-name">
                    ${this.escapeHtml(player.name)}
                    ${player.is_vip ? '<span class="vip-badge">VIP</span>' : ''}
                </div>
                <div class="player-status">
                    ${player.is_vip ? 'Can start the game' : 'Ready to play'}
                </div>
            `;
            
            playersContainer.appendChild(playerCard);
        });
        
        // Show message if no players
        if (realPlayers.length === 0) {
            playersContainer.innerHTML = '<div class="player-card"><div class="player-name">Waiting for players...</div></div>';
        }
    }

    // Update waiting message
    updateWaitingMessage() {
        const messageElement = document.getElementById('waiting-message');
        if (!messageElement) return;

        const realPlayers = this.gameState.players.filter(p => p.name !== 'TV_HOST');
        const vipPlayer = realPlayers.find(p => p.is_vip);

        if (realPlayers.length === 0) {
            messageElement.textContent = 'Waiting for players to join...';
        } else if (realPlayers.length === 1) {
            messageElement.textContent = 'Waiting for more players to join...';
        } else if (vipPlayer) {
            messageElement.textContent = `Waiting for ${vipPlayer.name} (VIP) to start the game...`;
        } else {
            messageElement.textContent = 'Waiting for game to start...';
        }
    }

    // Handle game started event
    handleGameStarted(data) {
        console.log('Game started event:', data);
        this.gameState.gameStatus = 'playing';

        // Only reset questionNumber if we haven't already received a question
        // This handles the race condition where new_question arrives before game_started
        if (!this.gameState.currentQuestion) {
            this.gameState.questionNumber = 0;
        } else {
            console.log('[RACE] new_question arrived before game_started, preserving questionNumber:', this.gameState.questionNumber);
        }

        // Switch to game screen
        this.showGameScreen();
    }

    // Handle new question
    handleNewQuestion(data) {
        console.log('New question received:', data);

        // Guard against duplicate question events - check if this is the same question we just received
        if (this.gameState.currentQuestion &&
            this.gameState.currentQuestion.id === data.question.id) {
            console.log('[GUARD] Ignoring duplicate question:', data.question.id);
            return;
        }

        this.gameState.currentQuestion = data.question;
        this.gameState.questionNumber++;

        // Reset answered state for all players
        this.gameState.players.forEach(player => {
            player.hasAnswered = false;
        });

        // Ensure game screen is shown (important for rematch when TV might be on waiting screen)
        if (this.gameState.gameStatus !== 'playing') {
            this.gameState.gameStatus = 'playing';
            this.showGameScreen();
        }

        this.displayQuestion(data.question, data.start_time);
        this.displayPlayerAvatars();
    }

    // Display question on TV
    displayQuestion(question, startTime) {
        // Hide results overlay from previous question
        const resultsOverlay = document.getElementById('tv-results-overlay');
        if (resultsOverlay) {
            resultsOverlay.classList.add('hidden');
            resultsOverlay.style.display = 'none';
        }

        // Clear player answer status from previous question
        const avatarsContainer = document.getElementById('player-avatars');
        if (avatarsContainer) {
            avatarsContainer.querySelectorAll('.player-avatar').forEach(avatar => {
                avatar.classList.remove('correct-answer', 'incorrect-answer', 'answered');
            });
        }

        // Reset player answered state
        this.gameState.players.forEach(player => {
            player.hasAnswered = false;
        });

        // Update question number
        document.getElementById('question-number').textContent = this.gameState.questionNumber;

        // Update category
        const categoryElement = document.getElementById('tv-question-category');
        if (categoryElement) {
            categoryElement.textContent = this.capitalizeFirst(question.category.replace('_', ' '));
        }

        // Update question text
        const questionTextElement = document.getElementById('tv-question-text');
        if (questionTextElement) {
            questionTextElement.textContent = question.text;
        }

        // Display answer options
        this.displayAnswerOptions(question.options);

        // Display initial time but don't start counting - wait for start_timer event
        const timerElement = document.getElementById('tv-timer');
        if (timerElement) {
            // Always show 30 seconds initially
            const timeLimit = 30;
            timerElement.textContent = timeLimit;
            console.log('[TIMER] Question displayed, showing initial time: 30 - waiting for start_timer event');
        }
    }

    // Display answer options on TV
    displayAnswerOptions(options) {
        const answersContainer = document.getElementById('tv-answers-grid');
        if (!answersContainer) return;

        answersContainer.innerHTML = '';

        // Sort options by their order property to ensure consistent display across all devices
        const sortedOptions = [...options].sort((a, b) => a.order - b.order);

        sortedOptions.forEach((option, index) => {
            const optionElement = document.createElement('div');
            optionElement.className = 'tv-answer-option';
            optionElement.textContent = `${String.fromCharCode(65 + index)}) ${option.text}`;
            optionElement.dataset.optionId = option.id;

            answersContainer.appendChild(optionElement);
        });
    }

    // Handle start timer event from server
    handleStartTimer(data) {
        console.log('[TIMER] Starting timer now that all players have received question:', data);
        // Always use exactly 30 seconds regardless of what the server sends
        const timeLimit = 30;
        console.log('[TIMER] Using fixed 30 second timer');
        this.startQuestionTimer(timeLimit);
    }

    // Start question timer
    startQuestionTimer(timeLimit) {
        const timerElement = document.getElementById('tv-timer');
        if (!timerElement) {
            console.error('[TIMER] Timer element not found!');
            return;
        }

        console.log('[TIMER] Starting timer with', timeLimit, 'seconds');

        // Clear any existing timer to prevent overlaps
        if (this.timerInterval) {
            console.log('[TIMER] Clearing existing timer interval');
            clearInterval(this.timerInterval);
            this.timerInterval = null;
        }

        let timeRemaining = timeLimit;
        timerElement.textContent = timeRemaining;
        console.log('[TIMER] Set initial display to', timeRemaining);

        this.timerInterval = setInterval(() => {
            timeRemaining--;
            timerElement.textContent = timeRemaining;
            console.log('[TIMER] Countdown:', timeRemaining);

            if (timeRemaining <= 0) {
                console.log('[TIMER] Timer reached 0 - broadcasting timeout');
                clearInterval(this.timerInterval);
                this.timerInterval = null;

                // Broadcast timer expired to all players for instant feedback
                this.broadcastTimerExpired();
            }
        }, 1000);

        console.log('[TIMER] Timer interval started, ID:', this.timerInterval);
    }

    // Broadcast timer expired event to all players
    async broadcastTimerExpired() {
        if (!this.gameState.roomCode || !this.gameState.currentQuestion) {
            return;
        }

        console.log('[TIMER EXPIRED] Broadcasting timeout to all players');

        // The broadcast is handled by WebSocket, but we can also make an API call
        // to ensure the server knows the timer expired
        try {
            await fetch(`${CONFIG.API_BASE_URL}/api/game/${this.gameState.roomCode}/timer-expired`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    question_id: this.gameState.currentQuestion.id
                })
            });
        } catch (error) {
            console.error('[TIMER EXPIRED] Error notifying server:', error);
        }
    }

    // Handle question results
    handleQuestionResults(data) {
        console.log('Question results:', data);

        // Clear the timer when results arrive (all players have answered or time is up)
        if (this.timerInterval) {
            clearInterval(this.timerInterval);
            this.timerInterval = null;
        }

        // Update player scores from leaderboard
        if (data.leaderboard) {
            data.leaderboard.forEach(leaderboardPlayer => {
                const player = this.gameState.players.find(p => p.id === leaderboardPlayer.player_id);
                if (player) {
                    player.total_score = leaderboardPlayer.total_score;
                }
            });

            // Refresh avatar display to show updated scores
            this.displayPlayerAvatars();
        }

        // Highlight correct answer
        const answersContainer = document.getElementById('tv-answers-grid');
        if (answersContainer && data.correct_answer) {
            const answerOptions = answersContainer.querySelectorAll('.tv-answer-option');
            answerOptions.forEach(option => {
                const optionId = parseInt(option.dataset.optionId);
                const isCorrect = data.correct_answer.id === optionId;

                if (isCorrect) {
                    option.classList.add('correct');
                }
            });
        }

        // Show player results (who was correct/incorrect)
        this.showPlayerResults(data);
    }

    // Show player results after a question
    showPlayerResults(data) {
        const results = data.results || [];

        // Separate safe (correct) and at-risk (incorrect) players
        const safePlayers = results.filter(r => r.is_correct && !r.is_ghost);
        const atRiskPlayers = results.filter(r => !r.is_correct && !r.is_ghost);

        console.log('[TV] Question results - Safe:', safePlayers.map(p => p.player_name));
        console.log('[TV] Question results - At-risk:', atRiskPlayers.map(p => p.player_name));

        // Update player avatars with correct/incorrect status
        const avatarsContainer = document.getElementById('player-avatars');
        if (avatarsContainer) {
            results.forEach(result => {
                const avatar = avatarsContainer.querySelector(`.player-avatar[data-player-id="${result.player_id}"]`);
                if (avatar) {
                    // Remove previous status classes
                    avatar.classList.remove('correct-answer', 'incorrect-answer');

                    if (!result.is_ghost) {
                        if (result.is_correct) {
                            avatar.classList.add('correct-answer');
                        } else {
                            avatar.classList.add('incorrect-answer');
                        }
                    }
                }
            });
        }

        // Show results overlay
        const resultsOverlay = document.getElementById('tv-results-overlay');
        if (resultsOverlay) {
            let html = '<div class="question-results-content">';

            if (safePlayers.length > 0) {
                html += `
                    <div class="safe-players-result">
                        <h3>✅ Safe</h3>
                        <p>${safePlayers.map(p => this.escapeHtml(p.player_name)).join(', ')}</p>
                    </div>
                `;
            }

            if (atRiskPlayers.length > 0) {
                html += `
                    <div class="at-risk-players-result">
                        <h3>⚠️ At Risk</h3>
                        <p>${atRiskPlayers.map(p => this.escapeHtml(p.player_name)).join(', ')}</p>
                    </div>
                `;
            }

            if (safePlayers.length === 0 && atRiskPlayers.length === 0) {
                html += '<p>Waiting for results...</p>';
            }

            html += '</div>';
            resultsOverlay.innerHTML = html;
            resultsOverlay.classList.remove('hidden');
            resultsOverlay.style.display = 'flex';
        }
    }

    // Load leaderboard
    async loadLeaderboard() {
        try {
            const response = await fetch(`${CONFIG.API_BASE_URL}/api/leaderboard`);
            if (response.ok) {
                const leaderboard = await response.json();
                this.displayLeaderboard(leaderboard);
            } else {
                console.log('No leaderboard data available');
                this.displayEmptyLeaderboard();
            }
        } catch (error) {
            console.error('Error loading leaderboard:', error);
            this.displayEmptyLeaderboard();
        }
    }

    // Display leaderboard
    displayLeaderboard(leaderboard) {
        const container = document.getElementById('leaderboard-container');
        if (!container) return;

        if (!leaderboard || leaderboard.length === 0) {
            container.innerHTML = '<div class="loading-leaderboard">No games played yet</div>';
            return;
        }

        container.innerHTML = '';
        
        // Show top 5 players
        leaderboard.slice(0, 5).forEach((player, index) => {
            const item = document.createElement('div');
            item.className = 'leaderboard-item';
            
            const rank = index + 1;
            const medal = rank === 1 ? '🥇' : rank === 2 ? '🥈' : rank === 3 ? '🥉' : `${rank}.`;
            
            item.innerHTML = `
                <div class="leaderboard-rank">${medal}</div>
                <div class="leaderboard-name">${this.escapeHtml(player.name)}</div>
                <div class="leaderboard-score">${player.score} pts</div>
            `;
            
            container.appendChild(item);
        });
    }

    // Display empty leaderboard
    displayEmptyLeaderboard() {
        const container = document.getElementById('leaderboard-container');
        if (container) {
            container.innerHTML = '<div class="loading-leaderboard">No games played yet<br>Be the first to play!</div>';
        }
    }

    // Display player avatars - unicorns for living players, ghosts for eliminated
    displayPlayerAvatars() {
        const avatarsContainer = document.getElementById('player-avatars');
        if (!avatarsContainer) return;

        avatarsContainer.innerHTML = '';

        const unicornColors = ['red', 'blue', 'green', 'yellow', 'purple', 'pink', 'orange', 'teal', 'indigo', 'lime'];
        const realPlayers = this.gameState.players.filter(p => p.name !== 'TV_HOST');

        realPlayers.forEach((player, index) => {
            const color = unicornColors[index % unicornColors.length];
            const avatarCard = document.createElement('div');
            avatarCard.className = 'player-avatar-card';
            avatarCard.dataset.playerId = player.id;

            // Show ghost emoji for ghost players, unicorn for living players
            const isGhost = player.is_ghost || false;
            const emoji = isGhost ? '👻' : '🦄';
            const ghostClass = isGhost ? 'ghost-player' : '';

            avatarCard.innerHTML = `
                <div class="player-avatar unicorn-${color} ${player.hasAnswered ? 'answered' : ''} ${ghostClass}" data-player-id="${player.id}">
                    ${emoji}
                </div>
                <div class="player-avatar-name">${this.escapeHtml(player.name)}</div>
                <div class="avatar-score">${player.total_score || 0} pts</div>
            `;

            avatarsContainer.appendChild(avatarCard);
        });
    }

    // Handle player answered event
    handlePlayerAnswered(data) {
        console.log('Player answered:', data);

        // Update player answered state
        const player = this.gameState.players.find(p => p.id == data.player_id);
        if (player) {
            player.hasAnswered = true;

            // Update avatar opacity
            const avatar = document.querySelector(`.player-avatar[data-player-id="${data.player_id}"]`);
            if (avatar) {
                avatar.classList.add('answered');
            }
        }
    }

    // Handle game ended event
    handleGameEnded(data) {
        console.log('Game ended:', data);
        this.gameState.gameStatus = 'finished';

        // Stop player polling
        if (this.pollingInterval) {
            clearInterval(this.pollingInterval);
            this.pollingInterval = null;
        }

        // Clean up haunting race if it's active
        const hauntingRaceScreen = document.getElementById('haunting-race-screen');
        if (hauntingRaceScreen) {
            hauntingRaceScreen.classList.add('hidden');
            hauntingRaceScreen.classList.remove('active');
        }

        // Clean up haunting race manager if it exists
        if (window.hauntingRaceManager) {
            window.hauntingRaceManager.cleanup();
        }

        // Hide all game screens, show game over screen
        document.getElementById('tv-game-screen').classList.add('hidden');
        document.getElementById('tv-game-over-screen').classList.remove('hidden');

        // Auto-return to home screen after 30 seconds if no rematch
        if (this.autoReturnTimeout) {
            clearTimeout(this.autoReturnTimeout);
        }
        this.autoReturnTimeout = setTimeout(() => {
            console.log('[AUTO-RETURN] No rematch requested, returning to home screen...');
            this.autoFinishGame();
        }, 30000); // 30 seconds

        // Show final leaderboard
        if (data.final_leaderboard && data.final_leaderboard.length > 0) {
            console.log('Final leaderboard:', data.final_leaderboard);

            // Display winner (first place)
            const winner = data.final_leaderboard[0];
            const winnerDisplay = document.getElementById('winner-display');
            const unicornColors = ['red', 'blue', 'green', 'yellow', 'purple', 'pink', 'orange', 'teal', 'indigo', 'lime'];
            const winnerColor = unicornColors[0]; // Winner gets the first color
            const winnerIsGhost = winner.is_ghost || false;
            const winnerEmoji = winnerIsGhost ? '👻' : '🦄';

            if (winnerDisplay) {
                winnerDisplay.innerHTML = `
                    <div class="winner-avatar unicorn-${winnerColor} ${winnerIsGhost ? 'ghost-player' : ''}">${winnerEmoji}</div>
                    <div class="winner-name">${this.escapeHtml(winner.player_name)}</div>
                    <div class="winner-score">${winner.total_score} points</div>
                `;
            }

            // Display final standings
            const finalLeaderboard = document.getElementById('final-leaderboard');
            if (finalLeaderboard) {
                finalLeaderboard.innerHTML = '';

                data.final_leaderboard.forEach((player, index) => {
                    const rank = index + 1;
                    const medal = rank === 1 ? '🥇' : rank === 2 ? '🥈' : rank === 3 ? '🥉' : `${rank}.`;
                    const color = unicornColors[index % unicornColors.length];
                    const isGhost = player.is_ghost || false;
                    const emoji = isGhost ? '👻' : '🦄';

                    const item = document.createElement('div');
                    item.className = 'final-standing-item';
                    item.innerHTML = `
                        <div class="final-standing-rank">${medal}</div>
                        <div class="final-standing-avatar unicorn-${color} ${isGhost ? 'ghost-player' : ''}">${emoji}</div>
                        <div class="final-standing-name">${this.escapeHtml(player.player_name)}</div>
                        <div class="final-standing-score">${player.total_score} pts</div>
                    `;

                    finalLeaderboard.appendChild(item);
                });
            }

            // Hide rematch button - VIP controls rematch from mobile
            // But show Finish Game button on TV so TV can end the session
            const rematchBtn = document.getElementById('rematch-btn');
            const finishBtn = document.getElementById('finish-game-btn');

            if (rematchBtn) rematchBtn.classList.add('hidden');
            if (finishBtn) finishBtn.classList.remove('hidden');
        }
    }

    // Handle mini-game start
    handleMiniGameStart(data) {
        console.log('[TV] Mini-game starting:', data.game_name);

        // Hide question results overlay when mini-game starts
        const resultsOverlay = document.getElementById('tv-results-overlay');
        if (resultsOverlay) {
            resultsOverlay.classList.add('hidden');
            resultsOverlay.style.display = 'none';
        }

        // Show mini-game overlay on TV
        const gameScreen = document.getElementById('tv-game-screen');
        if (!gameScreen) return;

        // Create or update mini-game display
        let miniGameOverlay = document.getElementById('tv-mini-game-overlay');
        if (!miniGameOverlay) {
            miniGameOverlay = document.createElement('div');
            miniGameOverlay.id = 'tv-mini-game-overlay';
            miniGameOverlay.className = 'tv-mini-game-overlay';
            gameScreen.appendChild(miniGameOverlay);
        }

        const setup = data.setup || {};
        const atRiskPlayers = setup.at_risk_players || [];
        const safePlayers = setup.safe_players || [];
        const racers = setup.racers || [];
        const gameMode = setup.game_mode || '';

        // Get player names
        const getPlayerName = (playerId) => {
            const player = this.gameState.players.find(p => p.id === playerId);
            return player ? player.name : `Player ${playerId}`;
        };

        // Store racer info for live score updates
        this.miniGameRacers = racers;
        this.miniGameScores = {};
        racers.forEach(id => this.miniGameScores[id] = 0);

        const atRiskNames = atRiskPlayers.map(id => this.escapeHtml(getPlayerName(id))).join(', ');
        const safeNames = safePlayers.map(id => this.escapeHtml(getPlayerName(id))).join(', ');

        // Quick Math specific display
        let gameSpecificHtml = '';
        if (data.game_name === 'Quick Math') {
            // Build scoreboard for Quick Math
            let scoreboardHtml = '<div class="quick-math-scoreboard">';
            racers.forEach(id => {
                const isAtRisk = atRiskPlayers.includes(id);
                scoreboardHtml += `
                    <div class="racer-score ${isAtRisk ? 'at-risk' : 'safe'}" data-player-id="${id}">
                        <span class="racer-name">${this.escapeHtml(getPlayerName(id))}</span>
                        <span class="racer-points" id="racer-score-${id}">0</span>
                        ${isAtRisk ? '<span class="at-risk-badge">⚠️</span>' : ''}
                    </div>
                `;
            });
            scoreboardHtml += '</div>';

            const modeText = gameMode === 'at_risk_vs_at_risk'
                ? 'Lowest scorer becomes a ghost!'
                : 'At-risk player must place 1st to survive!';

            gameSpecificHtml = `
                <div class="quick-math-tv-display">
                    <h3>🧮 Answer math questions as fast as you can!</h3>
                    <p class="mode-info">${modeText}</p>
                    <h4>Live Scores:</h4>
                    ${scoreboardHtml}
                </div>
            `;
        }

        miniGameOverlay.innerHTML = `
            <div class="mini-game-tv-content">
                <h2 class="mini-game-title">⚡ ${this.escapeHtml(data.game_name || 'Mini-Game')}</h2>

                <div class="mini-game-timer-large">
                    <span id="mini-game-tv-timer">${data.timeout || 45}</span>
                </div>

                ${gameSpecificHtml || `
                    <p class="mini-game-description">${this.escapeHtml(data.description || '')}</p>
                    <div class="mini-game-players">
                        <div class="at-risk-section">
                            <h3>⚠️ At Risk</h3>
                            <p>${atRiskNames || 'None'}</p>
                        </div>
                        <div class="safe-section">
                            <h3>✅ Safe</h3>
                            <p>${safeNames || 'None'}</p>
                        </div>
                    </div>
                `}
            </div>
        `;

        miniGameOverlay.style.display = 'flex';

        // Start countdown timer
        this.miniGameTimeRemaining = data.timeout || 45;
        if (this.miniGameTimerInterval) {
            clearInterval(this.miniGameTimerInterval);
        }
        this.miniGameTimerInterval = setInterval(() => {
            this.miniGameTimeRemaining--;
            const timerEl = document.getElementById('mini-game-tv-timer');
            if (timerEl) {
                timerEl.textContent = Math.max(0, this.miniGameTimeRemaining);
                if (this.miniGameTimeRemaining <= 10) {
                    timerEl.classList.add('timer-warning');
                }
            }
            if (this.miniGameTimeRemaining <= 0) {
                clearInterval(this.miniGameTimerInterval);
            }
        }, 1000);
    }

    // Handle mini-game player action (score updates, etc.)
    handleMiniGamePlayerAction(data) {
        console.log('[TV] Mini-game player action:', data);

        // Update live scores for Quick Math
        if (data.action && data.action.type === 'answer' && data.action.is_correct) {
            const playerId = data.player_id;
            if (this.miniGameScores && this.miniGameScores.hasOwnProperty(playerId)) {
                this.miniGameScores[playerId]++;
                const scoreEl = document.getElementById(`racer-score-${playerId}`);
                if (scoreEl) {
                    scoreEl.textContent = this.miniGameScores[playerId];
                    scoreEl.classList.add('score-flash');
                    setTimeout(() => scoreEl.classList.remove('score-flash'), 300);
                }
            }
        }
    }

    // Handle mini-game results
    handleMiniGameResults(data) {
        console.log('[TV] Mini-game results:', data);

        // Stop timer
        if (this.miniGameTimerInterval) {
            clearInterval(this.miniGameTimerInterval);
        }

        const miniGameOverlay = document.getElementById('tv-mini-game-overlay');
        if (miniGameOverlay) {
            // Data comes directly on data object, not data.results
            // eliminated is array of {player_id, player_name} objects
            const eliminated = data.eliminated || [];
            const survivors = data.survivors || [];
            const gameData = data.game_data || {};
            const gameName = data.game_name || 'Mini-Game';

            const getPlayerName = (playerId) => {
                const player = this.gameState.players.find(p => p.id === playerId);
                return player ? player.name : `Player ${playerId}`;
            };

            // Build game-specific details
            let gameSpecificHtml = '';

            if (gameName === 'Chalices' && gameData.poisoned_chalices) {
                // Show Chalices-specific results
                const poisonedChalices = gameData.poisoned_chalices || [];
                const testerResults = gameData.tester_results || {};
                const poisonerChoices = gameData.poisoner_choices || {};
                const numChalices = gameData.num_chalices || 3;

                // Build chalice visualization
                let chalicesHtml = '<div class="tv-chalices-display">';
                for (let i = 0; i < numChalices; i++) {
                    const isPoisoned = poisonedChalices.includes(i);
                    const chaliceClass = isPoisoned ? 'poisoned' : 'safe';
                    chalicesHtml += `
                        <div class="tv-chalice ${chaliceClass}">
                            <span class="tv-chalice-icon">${isPoisoned ? '☠️' : '🍷'}</span>
                            <span class="tv-chalice-num">${i + 1}</span>
                        </div>
                    `;
                }
                chalicesHtml += '</div>';

                // Show who chose what
                let choicesHtml = '<div class="tv-chalice-choices">';

                // Tester choices
                for (const [playerId, result] of Object.entries(testerResults)) {
                    const playerName = getPlayerName(parseInt(playerId));
                    const chaliceNum = result.chalice + 1;
                    const wasPoisoned = result.poisoned;
                    choicesHtml += `
                        <div class="tv-choice ${wasPoisoned ? 'eliminated' : 'survived'}">
                            <span class="choice-player">${this.escapeHtml(playerName)}</span>
                            <span class="choice-action">drank from Chalice ${chaliceNum}</span>
                            <span class="choice-result">${wasPoisoned ? '☠️ POISONED' : '✅ SAFE'}</span>
                        </div>
                    `;
                }
                choicesHtml += '</div>';

                gameSpecificHtml = `
                    <div class="chalices-results-detail">
                        <h3>🍷 Chalices Revealed</h3>
                        ${chalicesHtml}
                        <h4>Player Choices:</h4>
                        ${choicesHtml}
                    </div>
                `;
            }

            // Worst Answer specific results - show answers with player names and votes
            if (gameName === 'Worst Answer' && gameData.submitted_answers) {
                const submittedAnswers = gameData.submitted_answers || {};
                const voteCounts = gameData.vote_counts || {};
                const eliminatedPlayerId = eliminated.length > 0 ? eliminated[0].player_id : null;

                let answersHtml = '<div class="worst-answer-results">';
                answersHtml += '<h3>💭 Submitted Answers & Votes</h3>';
                answersHtml += '<div class="worst-answer-cards">';

                // Sort by vote count (highest first)
                const sortedAnswers = Object.entries(submittedAnswers).sort((a, b) => {
                    const votesA = voteCounts[a[0]] || 0;
                    const votesB = voteCounts[b[0]] || 0;
                    return votesB - votesA;
                });

                sortedAnswers.forEach(([playerId, answer]) => {
                    const playerName = getPlayerName(parseInt(playerId));
                    const votes = voteCounts[playerId] || 0;
                    const isEliminated = parseInt(playerId) === eliminatedPlayerId;

                    answersHtml += `
                        <div class="worst-answer-card ${isEliminated ? 'eliminated-answer' : ''}">
                            <div class="answer-text-result">"${this.escapeHtml(answer)}"</div>
                            <div class="answer-author-result">- ${this.escapeHtml(playerName)}</div>
                            <div class="vote-count">${votes} vote${votes !== 1 ? 's' : ''} ${isEliminated ? '👻' : ''}</div>
                        </div>
                    `;
                });

                answersHtml += '</div>';
                answersHtml += '</div>';

                gameSpecificHtml = answersHtml;
            }

            // Quick Math specific results
            if (gameName === 'Quick Math' && gameData.sorted_results) {
                const sortedResults = gameData.sorted_results || [];
                const eliminationReason = gameData.elimination_reason || '';

                let resultsHtml = '<div class="quick-math-results">';
                resultsHtml += '<h3>🏆 Final Scores</h3>';
                resultsHtml += '<div class="final-scoreboard">';

                sortedResults.forEach((result, index) => {
                    const playerName = getPlayerName(result.player_id);
                    const isEliminated = eliminated.some(e => e.player_id === result.player_id);
                    const medal = index === 0 ? '🥇' : index === 1 ? '🥈' : index === 2 ? '🥉' : '';

                    resultsHtml += `
                        <div class="final-score-row ${isEliminated ? 'eliminated' : ''}">
                            <span class="rank">${medal || (index + 1)}</span>
                            <span class="player-name">${this.escapeHtml(playerName)}</span>
                            <span class="final-points">${result.score} pts</span>
                            ${isEliminated ? '<span class="ghost-badge">👻</span>' : ''}
                        </div>
                    `;
                });

                resultsHtml += '</div>';
                if (eliminationReason) {
                    resultsHtml += `<p class="elimination-reason">${this.escapeHtml(eliminationReason)}</p>`;
                }
                resultsHtml += '</div>';

                gameSpecificHtml = resultsHtml;
            }

            // Pattern Tiles specific results
            if (gameName === 'Pattern Tiles' && gameData.pattern) {
                const pattern = gameData.pattern || [];
                const accuracies = gameData.accuracies || {};
                const sortedResults = gameData.sorted_results || [];
                const eliminationReason = gameData.elimination_reason || '';

                // Render the original pattern as a mini grid
                const renderMiniGrid = (grid) => {
                    let html = '<div class="tv-pattern-grid">';
                    for (let i = 0; i < 4; i++) {
                        for (let j = 0; j < 4; j++) {
                            const tileValue = grid[i][j];
                            const tileClass = tileValue === 1 ? 'tile-blue' : 'tile-white';
                            html += `<div class="tv-tile ${tileClass}"></div>`;
                        }
                    }
                    html += '</div>';
                    return html;
                };

                let resultsHtml = '<div class="pattern-tiles-results">';

                // Show the target pattern
                resultsHtml += '<div class="pattern-target">';
                resultsHtml += '<h3>🎯 Target Pattern</h3>';
                resultsHtml += renderMiniGrid(pattern);
                resultsHtml += '</div>';

                // Show player results sorted by accuracy
                resultsHtml += '<div class="pattern-scores">';
                resultsHtml += '<h3>📊 Accuracy Results</h3>';

                sortedResults.forEach((result, index) => {
                    const playerName = getPlayerName(result.player_id);
                    const accuracy = result.accuracy;
                    const isEliminated = eliminated.some(e => e.player_id === result.player_id);
                    const medal = index === 0 ? '🥇' : index === 1 ? '🥈' : index === 2 ? '🥉' : '';

                    resultsHtml += `
                        <div class="pattern-score-row ${isEliminated ? 'eliminated' : ''}">
                            <span class="rank">${medal || (index + 1)}</span>
                            <span class="player-name">${this.escapeHtml(playerName)}</span>
                            <span class="accuracy-bar">
                                <span class="accuracy-fill" style="width: ${accuracy}%"></span>
                            </span>
                            <span class="accuracy-value">${accuracy.toFixed(1)}%</span>
                            ${isEliminated ? '<span class="ghost-badge">👻</span>' : ''}
                        </div>
                    `;
                });

                resultsHtml += '</div>';

                if (eliminationReason) {
                    resultsHtml += `<p class="elimination-reason">${this.escapeHtml(eliminationReason)}</p>`;
                }
                resultsHtml += '</div>';

                gameSpecificHtml = resultsHtml;
            }

            miniGameOverlay.innerHTML = `
                <div class="mini-game-tv-content">
                    <h2 class="mini-game-title">🏁 ${this.escapeHtml(gameName)} - Results!</h2>

                    ${gameSpecificHtml}

                    <div class="mini-game-results">
                        ${eliminated.length > 0 ? `
                            <div class="eliminated-section">
                                <h3>👻 Became Ghosts</h3>
                                <p>${eliminated.map(e => this.escapeHtml(e.player_name || getPlayerName(e.player_id))).join(', ')}</p>
                            </div>
                        ` : `
                            <div class="no-eliminations">
                                <h3>🎉 Everyone Survived!</h3>
                            </div>
                        `}
                        ${survivors.length > 0 && eliminated.length > 0 ? `
                            <div class="survivors-section">
                                <h3>✅ Survived</h3>
                                <p>${survivors.map(id => this.escapeHtml(getPlayerName(id))).join(', ')}</p>
                            </div>
                        ` : ''}
                    </div>

                    <p class="next-round-message">Next question coming up...</p>
                </div>
            `;

            // Hide overlay after 5 seconds (longer to show results)
            setTimeout(() => {
                miniGameOverlay.style.display = 'none';
            }, 5000);
        }

        // Update player ghost status
        // eliminated is array of {player_id, player_name} objects
        if (data.eliminated && data.eliminated.length > 0) {
            data.eliminated.forEach(e => {
                const playerId = e.player_id;
                const player = this.gameState.players.find(p => p.id === playerId);
                if (player) {
                    player.is_ghost = true;
                }
            });
            this.updatePlayersDisplay();
        }
    }

    // Handle mini-game timeout
    handleMiniGameTimeout(data) {
        console.log('[TV] Mini-game timeout:', data);
        // Results will follow, so just log for now
    }

    handleMiniGamePhaseChange(data) {
        console.log('[TV] Mini-game phase change:', data);

        // Handle Worst Answer voting phase - update TV display
        if (data.game_name === 'Worst Answer' && data.phase === 'voting') {
            const miniGameOverlay = document.getElementById('tv-mini-game-overlay');
            if (miniGameOverlay) {
                const answers = data.submitted_answers || {};
                const answerEntries = Object.entries(answers);

                // Hide player names during voting to prevent bias
                // Show only the answers with anonymous labels
                let answersHtml = answerEntries.map(([playerId, answer], index) => {
                    return `
                        <div class="tv-answer-card">
                            <div class="answer-label">Answer ${index + 1}</div>
                            <div class="answer-text">"${this.escapeHtml(answer)}"</div>
                        </div>
                    `;
                }).join('');

                miniGameOverlay.innerHTML = `
                    <div class="tv-mini-game-content">
                        <h1 class="mini-game-title">💭 Worst Answer - VOTING</h1>
                        <p class="mini-game-instructions">Players: Vote for the WORST answer!</p>
                        <p class="mini-game-note">(Names hidden to ensure unbiased voting)</p>
                        <div class="mini-game-timer-large">
                            <span id="tv-mini-game-timer">30</span>s
                        </div>
                        <div class="tv-answers-grid">
                            ${answersHtml}
                        </div>
                    </div>
                `;

                // Start voting timer
                if (this.miniGameTimerInterval) {
                    clearInterval(this.miniGameTimerInterval);
                }
                let votingTime = 20;
                this.miniGameTimerInterval = setInterval(() => {
                    votingTime--;
                    const timerEl = document.getElementById('tv-mini-game-timer');
                    if (timerEl) {
                        timerEl.textContent = votingTime;
                        if (votingTime <= 5) {
                            timerEl.parentElement.classList.add('timer-warning');
                        }
                    }
                    if (votingTime <= 0) {
                        clearInterval(this.miniGameTimerInterval);
                    }
                }, 1000);
            }
        }
    }

    // Handle rematch button click
    async handleRematch() {
        if (!this.gameState.roomCode || !this.hostPlayerId) {
            console.error('Missing room code or host player ID');
            return;
        }

        try {
            const response = await fetch(`${CONFIG.API_BASE_URL}/api/game/rematch`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    room_code: this.gameState.roomCode,
                    player_id: this.hostPlayerId
                })
            });

            if (!response.ok) {
                const error = await response.json();
                alert(error.detail || 'Failed to start rematch');
            }
        } catch (error) {
            console.error('Error starting rematch:', error);
            alert('Network error: ' + error.message);
        }
    }

    // Handle finish game button click
    async handleFinishGame() {
        if (!this.gameState.roomCode) {
            console.error('No active room to finish');
            return;
        }

        // Confirm the user wants to finish and delete the room
        const confirmFinish = confirm('Are you sure you want to finish and delete this room? All players will be disconnected.');
        if (!confirmFinish) {
            return;
        }

        try {
            console.log('[FINISH GAME] Finishing and deleting room:', this.gameState.roomCode);

            // Stop player polling
            this.stopPlayerPolling();

            // Disconnect WebSocket
            if (this.wsManager) {
                this.wsManager.disconnect();
            }

            // Delete the room via API (same as Exit Room)
            const response = await fetch(`${CONFIG.API_BASE_URL}/api/rooms/${this.gameState.roomCode}`, {
                method: 'DELETE'
            });

            if (response.ok) {
                console.log('[FINISH GAME] Room deleted successfully');
            } else {
                console.error('[FINISH GAME] Failed to delete room');
            }

            // Clear saved room code from localStorage
            localStorage.removeItem('tv_room_code');
            console.log('[FINISH GAME] Cleared saved room code');

            // Reset game state
            this.gameState = {
                roomCode: null,
                players: [],
                currentQuestion: null,
                questionNumber: 0,
                gameStatus: 'home'
            };

            // Return to home screen
            document.querySelectorAll('.screen').forEach(screen => {
                screen.classList.add('hidden');
            });
            document.getElementById('tv-home-screen').classList.remove('hidden');

            // Reload leaderboard
            this.loadLeaderboard();

            console.log('[FINISH GAME] Returned to home screen');

        } catch (error) {
            console.error('[FINISH GAME] Error finishing game:', error);
            alert('Failed to finish game. Please try again.');
        }
    }

    // Auto finish game (without confirmation) - called after timeout
    async autoFinishGame() {
        if (!this.gameState.roomCode) {
            console.error('[AUTO-FINISH] No active room to finish');
            return;
        }

        try {
            console.log('[AUTO-FINISH] Auto-finishing and deleting room:', this.gameState.roomCode);

            // Stop player polling
            this.stopPlayerPolling();

            // Disconnect WebSocket
            if (this.wsManager) {
                this.wsManager.disconnect();
            }

            // Delete the room via API
            const response = await fetch(`${CONFIG.API_BASE_URL}/api/rooms/${this.gameState.roomCode}`, {
                method: 'DELETE'
            });

            if (response.ok) {
                console.log('[AUTO-FINISH] Room deleted successfully');
            } else {
                console.error('[AUTO-FINISH] Failed to delete room');
            }

            // Clear saved room code from localStorage
            localStorage.removeItem('tv_room_code');
            console.log('[AUTO-FINISH] Cleared saved room code');

            // Reset game state
            this.gameState = {
                roomCode: null,
                players: [],
                currentQuestion: null,
                questionNumber: 0,
                gameStatus: 'home'
            };

            // Return to home screen
            document.querySelectorAll('.screen').forEach(screen => {
                screen.classList.add('hidden');
            });
            document.getElementById('tv-home-screen').classList.remove('hidden');

            // Reload leaderboard
            this.loadLeaderboard();

            console.log('[AUTO-FINISH] Returned to home screen');

        } catch (error) {
            console.error('[AUTO-FINISH] Error auto-finishing game:', error);
        }
    }

    // Handle reset leaderboard button click
    async handleResetLeaderboard() {
        // Confirm the user wants to reset the leaderboard
        const confirmReset = confirm('Are you sure you want to delete all high scores? This action cannot be undone.');
        if (!confirmReset) {
            return;
        }

        try {
            console.log('[RESET LEADERBOARD] Resetting leaderboard...');

            const response = await fetch(`${CONFIG.API_BASE_URL}/api/leaderboard`, {
                method: 'DELETE'
            });

            if (response.ok) {
                const data = await response.json();
                console.log('[RESET LEADERBOARD] Leaderboard reset successfully:', data);

                // Reload the leaderboard to show empty state
                await this.loadLeaderboard();

                alert(`Leaderboard reset successfully! Deleted ${data.deleted_count} high score(s).`);
            } else {
                console.error('[RESET LEADERBOARD] Failed to reset leaderboard');
                alert('Failed to reset leaderboard. Please try again.');
            }

        } catch (error) {
            console.error('[RESET LEADERBOARD] Error resetting leaderboard:', error);
            alert('Failed to reset leaderboard. Please check your connection.');
        }
    }

    // Handle emergency terminate button - force end game and delete room
    async handleEmergencyTerminate() {
        if (!this.gameState.roomCode) {
            console.error('No active room to terminate');
            return;
        }

        // Confirm the user wants to emergency terminate
        const confirmTerminate = confirm('⚠️ EMERGENCY TERMINATE\n\nThis will immediately end the game and disconnect all players.\n\nUse this only if the game is stuck or experiencing errors.\n\nAre you sure?');
        if (!confirmTerminate) {
            return;
        }

        try {
            console.log('[EMERGENCY TERMINATE] Force terminating room:', this.gameState.roomCode);

            // Clear timer
            if (this.timerInterval) {
                clearInterval(this.timerInterval);
                this.timerInterval = null;
            }

            // Stop player polling
            this.stopPlayerPolling();

            // Disconnect WebSocket
            if (this.wsManager) {
                this.wsManager.disconnect();
            }

            // Delete the room via API
            const response = await fetch(`${CONFIG.API_BASE_URL}/api/rooms/${this.gameState.roomCode}`, {
                method: 'DELETE'
            });

            if (response.ok) {
                console.log('[EMERGENCY TERMINATE] Room deleted successfully');
            } else {
                console.error('[EMERGENCY TERMINATE] Failed to delete room');
            }

            // Clear saved room code from localStorage
            localStorage.removeItem('tv_room_code');
            console.log('[EMERGENCY TERMINATE] Cleared saved room code');

            // Reset game state
            this.gameState = {
                roomCode: null,
                players: [],
                currentQuestion: null,
                questionNumber: 0,
                gameStatus: 'home'
            };

            // Return to home screen
            document.querySelectorAll('.screen').forEach(screen => {
                screen.classList.add('hidden');
            });
            document.getElementById('tv-home-screen').classList.remove('hidden');

            // Reload leaderboard
            this.loadLeaderboard();

            console.log('[EMERGENCY TERMINATE] Returned to home screen');
            alert('Room terminated successfully. All players have been disconnected.');

        } catch (error) {
            console.error('[EMERGENCY TERMINATE] Error terminating room:', error);
            alert('Failed to terminate room. Please try refreshing the page.');
        }
    }

    // Handle rematch started event from WebSocket
    handleRematchStarted(data) {
        console.log('Rematch starting:', data);

        // Cancel auto-return timer if rematch is starting
        if (this.autoReturnTimeout) {
            clearTimeout(this.autoReturnTimeout);
            this.autoReturnTimeout = null;
            console.log('[REMATCH] Cancelled auto-return timer');
        }

        // Stop player polling
        this.stopPlayerPolling();

        // Reset game state
        this.gameState.gameStatus = 'waiting';
        this.gameState.currentQuestion = null;
        this.gameState.questionNumber = 0;

        // Reset all player scores
        this.gameState.players.forEach(player => {
            player.total_score = 0;
            player.hasAnswered = false;
        });

        // Hide game over screen, show waiting screen
        document.getElementById('tv-game-over-screen').classList.add('hidden');
        document.getElementById('tv-waiting-screen').classList.remove('hidden');

        // Update players display
        this.updatePlayersDisplay();

        // Start polling for new players
        this.startPlayerPolling();
    }

    // Handle game finished event from WebSocket
    handleGameFinished(data) {
        console.log('Game finished by VIP:', data);

        // Stop player polling
        this.stopPlayerPolling();

        // Disconnect WebSocket
        if (this.wsManager) {
            this.wsManager.disconnect();
        }

        // Clear saved room code from localStorage
        localStorage.removeItem('tv_room_code');
        console.log('[TV SESSION] Cleared saved room code - game finished');

        // Reset game state
        this.gameState = {
            roomCode: null,
            players: [],
            currentQuestion: null,
            questionNumber: 0,
            gameStatus: 'home'
        };

        // Hide all screens, show home screen
        document.querySelectorAll('.screen').forEach(screen => {
            screen.classList.add('hidden');
        });
        document.getElementById('tv-home-screen').classList.remove('hidden');

        // Reload leaderboard
        this.loadLeaderboard();
    }

    // Utility functions
    shuffleArray(array) {
        const shuffled = [...array];
        for (let i = shuffled.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
        }
        return shuffled;
    }

    capitalizeFirst(str) {
        return str.charAt(0).toUpperCase() + str.slice(1);
    }

    escapeHtml(text) {
        const map = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#039;'
        };
        return text.replace(/[&<>"']/g, m => map[m]);
    }

    // Poll for player updates
    startPlayerPolling() {
        if (this.pollingInterval) {
            clearInterval(this.pollingInterval);
        }

        this.pollingInterval = setInterval(async () => {
            if (!this.gameState.roomCode) return;

            try {
                const response = await fetch(`${CONFIG.API_BASE_URL}/api/rooms/${this.gameState.roomCode}/players`);
                if (response.ok) {
                    const players = await response.json();
                    this.gameState.players = players;
                    this.updatePlayersDisplay();
                    this.updateWaitingMessage();
                }
            } catch (error) {
                console.error('Error polling players:', error);
            }
        }, 2000); // Poll every 2 seconds
    }

    stopPlayerPolling() {
        if (this.pollingInterval) {
            clearInterval(this.pollingInterval);
            this.pollingInterval = null;
        }
    }
}

// Initialize TV app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new TVApp();
});