// Haunting Race Game Logic
// Handles the endgame race between unicorn (living player) and ghosts

class HauntingRaceManager {
    constructor(wsManager, playerId, isTV = false) {
        this.wsManager = wsManager;
        this.playerId = playerId;
        this.isTV = isTV;

        // Game state
        this.isActive = false;
        this.raceData = null;
        this.currentQuestion = null;
        this.questionStartTime = null;
        this.timerInterval = null;
        this.selectedStatements = new Set();
        this.hasAnswered = false;
        this.positions = {};
        this.isUnicorn = false;
        this.updateCancelled = false;  // Flag to cancel pending position updates

        // DOM references (lazy loaded)
        this.elements = {};

        // Bind methods
        this.handleRaceStart = this.handleRaceStart.bind(this);
        this.handleQuestion = this.handleQuestion.bind(this);
        this.handlePositions = this.handlePositions.bind(this);
        this.handleUnicornSwap = this.handleUnicornSwap.bind(this);
        this.handleResults = this.handleResults.bind(this);
        this.handleRaceEnd = this.handleRaceEnd.bind(this);
        this.submitAnswer = this.submitAnswer.bind(this);

        // Register WebSocket event listeners
        this.registerEventListeners();
    }

    // Register WebSocket event listeners
    registerEventListeners() {
        this.wsManager.on('haunting_race_start', this.handleRaceStart);
        this.wsManager.on('haunting_race_question', this.handleQuestion);
        this.wsManager.on('haunting_race_positions', this.handlePositions);
        this.wsManager.on('haunting_race_unicorn_swap', this.handleUnicornSwap);
        this.wsManager.on('haunting_race_results', this.handleResults);
        this.wsManager.on('haunting_race_end', this.handleRaceEnd);
    }

    // Unregister WebSocket event listeners
    unregisterEventListeners() {
        this.wsManager.off('haunting_race_start', this.handleRaceStart);
        this.wsManager.off('haunting_race_question', this.handleQuestion);
        this.wsManager.off('haunting_race_positions', this.handlePositions);
        this.wsManager.off('haunting_race_unicorn_swap', this.handleUnicornSwap);
        this.wsManager.off('haunting_race_results', this.handleResults);
        this.wsManager.off('haunting_race_end', this.handleRaceEnd);
    }

    // Get DOM elements (lazy loading)
    getElements() {
        if (Object.keys(this.elements).length === 0) {
            this.elements = {
                screen: document.getElementById('haunting-race-screen'),
                title: document.querySelector('.haunting-race-title'),
                subtitle: document.querySelector('.haunting-race-subtitle'),
                trackContainer: document.querySelector('.race-track-container'),
                track: document.querySelector('.race-track'),
                questionSection: document.querySelector('.haunting-race-question-section'),
                questionNumber: document.querySelector('.question-number'),
                questionTimer: document.querySelector('.question-timer'),
                questionTopic: document.querySelector('.question-topic'),
                statementsContainer: document.querySelector('.statements-container'),
                submitBtn: document.querySelector('.submit-answer-btn'),
                resultsSection: document.querySelector('.haunting-race-results')
            };
        }
        return this.elements;
    }

    // Handle race start event
    handleRaceStart(data) {
        console.log('Haunting race started:', data);

        this.isActive = true;
        this.raceData = data.data;
        this.positions = this.raceData.initial_positions;
        this.isUnicorn = (this.raceData.unicorn_id == this.playerId);

        // Show haunting race screen
        this.showRaceScreen();

        // Initialize race track
        this.initializeRaceTrack();

        // Show intro message
        this.showIntroMessage();
    }

    // Show race screen
    showRaceScreen() {
        const elements = this.getElements();

        if (this.isTV) {
            // TV: hide other screens, show race screen
            document.querySelectorAll('.screen').forEach(screen => {
                screen.style.display = 'none';
            });
        } else {
            // Mobile: hide other screens
            const gameScreen = document.getElementById('game-screen');
            const waitingScreen = document.getElementById('waiting-screen');
            if (gameScreen) gameScreen.style.display = 'none';
            if (waitingScreen) waitingScreen.style.display = 'none';
        }

        if (elements.screen) {
            elements.screen.classList.add('active');
            elements.screen.classList.remove('hidden');
        }
    }

    // Initialize race track with 20 columns
    initializeRaceTrack() {
        const elements = this.getElements();
        if (!elements.track) return;

        elements.track.innerHTML = '';

        // Create 20 columns
        for (let col = 1; col <= 20; col++) {
            const column = document.createElement('div');
            column.className = 'race-column';
            column.dataset.column = col;

            // Mark special columns
            if (col === 20) {
                column.classList.add('finish-line');
            } else if (col <= 8) {
                column.classList.add('start-zone');
            }

            // Add column number
            const colNumber = document.createElement('div');
            colNumber.className = 'column-number';
            colNumber.textContent = col;
            column.appendChild(colNumber);

            elements.track.appendChild(column);
        }

        // Add player icons to their starting positions
        this.updatePlayerPositions(false); // No animation on initial render
    }

    // Update player positions on track
    async updatePlayerPositions(animate = true) {
        const elements = this.getElements();
        if (!elements.track) return;

        // Cancel any pending updates
        this.updateCancelled = true;
        await this.delay(10); // Give time for async operations to check flag

        // Reset cancellation flag for this update
        this.updateCancelled = false;

        // Remove existing player icons
        document.querySelectorAll('.race-player').forEach(el => el.remove());

        // Get player data
        const unicornId = this.raceData.unicorn_id;
        const ghostIds = this.raceData.ghost_ids;
        const players = this.raceData.players;

        console.log('[HAUNTING-RACE-UPDATE] Updating player positions - Unicorn:', unicornId, 'Ghosts:', ghostIds);

        // Add unicorn FIRST
        if (this.positions[unicornId]) {
            const unicornPlayer = players.find(p => p.id == unicornId);
            console.log('[HAUNTING-RACE-UPDATE] Adding UNICORN:', unicornPlayer?.name, 'at position', this.positions[unicornId]);
            this.addPlayerToTrack(unicornId, this.positions[unicornId], 'unicorn', unicornPlayer, animate);
        }

        // Wait before showing ghosts move (so players see unicorn moves first)
        if (animate) {
            await this.delay(2000); // 2 second delay

            // Check if this update was cancelled during the delay
            if (this.updateCancelled) {
                console.log('[HAUNTING-RACE-UPDATE] Update cancelled, skipping ghost rendering');
                return;
            }
        }

        // Add ALL ghosts at the same time (after unicorn)
        ghostIds.forEach(ghostId => {
            if (this.positions[ghostId]) {
                const ghostPlayer = players.find(p => p.id == ghostId);
                console.log('[HAUNTING-RACE-UPDATE] Adding GHOST:', ghostPlayer?.name, 'at position', this.positions[ghostId]);
                this.addPlayerToTrack(ghostId, this.positions[ghostId], 'ghost', ghostPlayer, animate);
            }
        });
    }

    // Helper function for delays
    delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    // Add player icon to specific column
    addPlayerToTrack(playerId, column, role, playerData, animate) {
        const elements = this.getElements();
        const columnEl = elements.track.querySelector(`[data-column="${column}"]`);
        if (!columnEl) return;

        const playerIcon = document.createElement('div');
        playerIcon.className = `race-player ${role}`;
        playerIcon.dataset.playerId = playerId;

        // Set icon based on role
        playerIcon.textContent = role === 'unicorn' ? '🦄' : '👻';

        // Add name tag
        const nameTag = document.createElement('div');
        nameTag.className = 'player-name-tag';
        nameTag.textContent = playerData ? playerData.name : `Player ${playerId}`;
        playerIcon.appendChild(nameTag);

        // Check if ghost is catching up (adjacent to unicorn)
        if (role === 'ghost') {
            const unicornPos = this.positions[this.raceData.unicorn_id];
            if (Math.abs(column - unicornPos) <= 1) {
                playerIcon.classList.add('catching');
            }
        }

        // Position player icon in column
        // On TV, stack players vertically from bottom
        if (this.isTV) {
            playerIcon.classList.add('tv-race-player');

            // Count existing players in this column
            const playersInColumn = columnEl.querySelectorAll('.race-player').length;

            // Stack from bottom: each player 50px above the previous
            const verticalOffset = playersInColumn * 50;  // 50px per player (45px icon + 5px gap)
            playerIcon.style.bottom = `${verticalOffset}px`;
        }

        columnEl.appendChild(playerIcon);

        // Add entrance animation if needed
        if (animate) {
            playerIcon.style.animation = 'none';
            setTimeout(() => {
                playerIcon.style.animation = '';
            }, 10);
        }
    }

    // Show intro message
    showIntroMessage() {
        const elements = this.getElements();

        if (this.isTV) {
            // TV shows full game state
            if (elements.title) {
                elements.title.textContent = '🏁 Haunting Race!';
            }
            if (elements.subtitle) {
                elements.subtitle.textContent = 'Unicorn must reach the finish line!';
            }
        } else {
            // Mobile shows role-specific message
            if (elements.title) {
                if (this.isUnicorn) {
                    elements.title.textContent = '🦄 You are the Unicorn!';
                } else {
                    elements.title.textContent = '👻 You are a Ghost!';
                }
            }
            if (elements.subtitle) {
                if (this.isUnicorn) {
                    elements.subtitle.textContent = 'Reach column 20 to win!';
                } else {
                    elements.subtitle.textContent = 'Catch the unicorn to swap roles!';
                }
            }
        }
    }

    // Handle new question
    handleQuestion(data) {
        console.log('Haunting race question:', data);

        this.currentQuestion = data.data;
        this.questionStartTime = Date.now();
        this.selectedStatements.clear();
        this.hasAnswered = false;
        this.isUnicorn = data.is_unicorn;

        // Show question section
        this.displayQuestion();

        // Start timer
        this.startTimer();
    }

    // Display question with statements
    displayQuestion() {
        const elements = this.getElements();
        if (!elements.questionSection) return;

        // Show question section
        elements.questionSection.style.display = 'block';
        if (elements.resultsSection) {
            elements.resultsSection.style.display = 'none';
        }

        // Update question header
        if (elements.questionNumber) {
            elements.questionNumber.textContent = `Question ${this.currentQuestion.question_number || ''}`;
        }

        if (elements.questionTopic) {
            elements.questionTopic.textContent = this.currentQuestion.question_text;
        }

        // For TV, show statements for viewing (non-interactive)
        if (this.isTV) {
            if (elements.statementsContainer) {
                elements.statementsContainer.innerHTML = '';
                const statements = this.currentQuestion.statements || [];

                statements.forEach(statement => {
                    const statementDiv = document.createElement('div');
                    statementDiv.className = 'statement-item tv-statement';
                    statementDiv.style.cssText = 'padding: 12px; margin: 8px 0; background: white; border-radius: 5px; border-left: 3px solid #2196F3;';

                    const textSpan = document.createElement('span');
                    textSpan.style.cssText = 'color: #333; font-size: 16px;';
                    textSpan.textContent = statement.text;

                    if (statement.is_ghost_only) {
                        const ghostBadge = document.createElement('span');
                        ghostBadge.textContent = ' 👻';
                        ghostBadge.style.cssText = 'font-size: 0.8em; margin-left: 5px;';
                        statementDiv.appendChild(textSpan);
                        statementDiv.appendChild(ghostBadge);
                    } else {
                        statementDiv.appendChild(textSpan);
                    }

                    elements.statementsContainer.appendChild(statementDiv);
                });
            }
            if (elements.submitBtn) {
                elements.submitBtn.style.display = 'none';
            }
        } else {
            // For mobile, display statements
            this.displayStatements();

            // Enable submit button (always enabled - empty selection = all false)
            if (elements.submitBtn) {
                elements.submitBtn.style.display = 'block';
                elements.submitBtn.disabled = false;
                elements.submitBtn.textContent = 'Submit Answer';
                elements.submitBtn.onclick = this.submitAnswer;
            }
        }
    }

    // Display true/false statements
    displayStatements() {
        const elements = this.getElements();
        if (!elements.statementsContainer) return;

        elements.statementsContainer.innerHTML = '';

        const statements = this.currentQuestion.statements || [];

        statements.forEach(statement => {
            const statementItem = document.createElement('div');
            statementItem.className = 'statement-item';
            statementItem.dataset.statementId = statement.id;

            // Mark ghost-only statements
            if (statement.is_ghost_only) {
                statementItem.classList.add('ghost-only');
            }

            // Checkbox
            const checkbox = document.createElement('div');
            checkbox.className = 'statement-checkbox';
            statementItem.appendChild(checkbox);

            // Statement text
            const text = document.createElement('div');
            text.className = 'statement-text';
            text.textContent = statement.text;
            statementItem.appendChild(text);

            // Click handler
            statementItem.addEventListener('click', () => {
                if (this.hasAnswered) return;

                this.toggleStatement(statement.id, statementItem);
            });

            elements.statementsContainer.appendChild(statementItem);
        });
    }

    // Toggle statement selection
    toggleStatement(statementId, statementItem) {
        if (this.selectedStatements.has(statementId)) {
            this.selectedStatements.delete(statementId);
            statementItem.classList.remove('selected');
        } else {
            this.selectedStatements.add(statementId);
            statementItem.classList.add('selected');
        }

        // Update submit button text based on selection
        const elements = this.getElements();
        if (elements.submitBtn) {
            if (this.selectedStatements.size > 0) {
                elements.submitBtn.textContent = 'Submit Answer';
            } else {
                elements.submitBtn.textContent = 'Submit Answer (All False)';
            }
            // Button always enabled - empty selection is valid (all false)
            elements.submitBtn.disabled = false;
        }
    }

    // Start question timer
    startTimer() {
        const elements = this.getElements();
        if (!elements.questionTimer) return;

        const timeLimit = this.currentQuestion.time_limit || 40;
        let timeRemaining = timeLimit;

        // Clear existing timer
        if (this.timerInterval) {
            clearInterval(this.timerInterval);
        }

        // Update timer display
        const updateTimerDisplay = () => {
            if (!elements.questionTimer) return;

            elements.questionTimer.textContent = `${timeRemaining}s`;

            // Add warning/danger classes
            elements.questionTimer.classList.remove('warning', 'danger');
            if (timeRemaining <= 5) {
                elements.questionTimer.classList.add('danger');
            } else if (timeRemaining <= 10) {
                elements.questionTimer.classList.add('warning');
            }
        };

        updateTimerDisplay();

        // Start countdown
        this.timerInterval = setInterval(() => {
            timeRemaining--;
            updateTimerDisplay();

            if (timeRemaining <= 0) {
                clearInterval(this.timerInterval);
                this.timerInterval = null;

                // Auto-submit if not answered
                if (!this.hasAnswered) {
                    this.submitAnswer();
                }
            }
        }, 1000);
    }

    // Submit answer
    async submitAnswer() {
        if (this.hasAnswered) return;

        this.hasAnswered = true;
        const responseTime = (Date.now() - this.questionStartTime) / 1000;

        // Clear timer
        if (this.timerInterval) {
            clearInterval(this.timerInterval);
            this.timerInterval = null;
        }

        // Disable all statements
        const elements = this.getElements();
        document.querySelectorAll('.statement-item').forEach(item => {
            item.classList.add('disabled');
        });

        // Disable submit button
        if (elements.submitBtn) {
            elements.submitBtn.disabled = true;
            elements.submitBtn.textContent = 'Submitted...';
        }

        // Send answer to backend
        try {
            const requestBody = {
                room_code: this.wsManager.roomCode,
                player_id: this.playerId,
                question_id: this.currentQuestion.question_id,
                selected_statement_ids: Array.from(this.selectedStatements),
                response_time: responseTime
            };

            console.log('[HAUNTING-RACE] Submitting answer:', requestBody);

            const response = await fetch(`${CONFIG.API_BASE_URL}/api/game/haunting-race/submit-answer`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(requestBody)
            });

            if (!response.ok) {
                const error = await response.json();
                console.error('[HAUNTING-RACE] Submit failed:', {
                    status: response.status,
                    statusText: response.statusText,
                    error: error
                });
                this.showNotification(`Failed to submit answer: ${error.detail || response.statusText}`, 'error');
            } else {
                const result = await response.json();
                console.log('[HAUNTING-RACE] Submit successful:', result);
            }
        } catch (error) {
            console.error('[HAUNTING-RACE] Network error submitting answer:', error);
            this.showNotification('Network error', 'error');
        }
    }

    // Handle position updates
    handlePositions(data) {
        console.log('Position update:', data);

        const positionData = data.data;
        this.positions = positionData.positions;

        // Update visual positions with animation
        this.updatePlayerPositions(true);
    }

    // Update role display (title and subtitle)
    updateRoleDisplay() {
        const elements = {
            title: document.querySelector('.haunting-race-title'),
            subtitle: document.querySelector('.haunting-race-subtitle')
        };

        // Mobile shows role-specific message
        if (elements.title) {
            if (this.isUnicorn) {
                elements.title.textContent = '🦄 You are the Unicorn!';
            } else {
                elements.title.textContent = '👻 You are a Ghost!';
            }
        }
        if (elements.subtitle) {
            if (this.isUnicorn) {
                elements.subtitle.textContent = 'Reach column 20 to win!';
            } else {
                elements.subtitle.textContent = 'Catch the unicorn to swap roles!';
            }
        }
    }

    // Handle unicorn swap
    handleUnicornSwap(data) {
        console.log('[HAUNTING-RACE-SWAP] Unicorn swap event received:', data);

        const swapData = data.data;

        console.log('[HAUNTING-RACE-SWAP] Old unicorn:', swapData.old_unicorn_id);
        console.log('[HAUNTING-RACE-SWAP] New unicorn:', swapData.new_unicorn_id);
        console.log('[HAUNTING-RACE-SWAP] New ghost IDs:', swapData.ghost_ids);

        // Update positions first
        this.positions = swapData.new_positions;
        this.raceData.unicorn_id = swapData.new_unicorn_id;

        // Update ghosts list
        this.raceData.ghost_ids = swapData.ghost_ids;

        // Check if we are the new unicorn
        this.isUnicorn = (swapData.new_unicorn_id == this.playerId);

        console.log('[HAUNTING-RACE-SWAP] Updated local state - Unicorn ID:', this.raceData.unicorn_id, 'Ghost IDs:', this.raceData.ghost_ids);

        // Update UI to reflect new role
        this.updateRoleDisplay();

        // Update player positions immediately (before animation)
        console.log('[HAUNTING-RACE-SWAP] Updating player positions on track...');
        this.updatePlayerPositions(false);

        // Show swap animation
        this.showSwapAnimation(swapData);
    }

    // Show unicorn swap animation
    showSwapAnimation(swapData) {
        // Create overlay
        const overlay = document.createElement('div');
        overlay.className = 'unicorn-swap-overlay';

        const message = document.createElement('div');
        message.className = 'unicorn-swap-message';

        const icon = document.createElement('div');
        icon.className = 'swap-icon';
        icon.textContent = '🔄';

        const text = document.createElement('div');
        text.className = 'swap-text';

        // Get player names
        const oldUnicornName = this.raceData.players.find(p => p.id == swapData.old_unicorn_id)?.name || 'Player';
        const newUnicornName = this.raceData.players.find(p => p.id == swapData.new_unicorn_id)?.name || 'Player';

        text.textContent = `${newUnicornName} caught the unicorn!\n${newUnicornName} is now the unicorn!`;

        message.appendChild(icon);
        message.appendChild(text);
        overlay.appendChild(message);

        document.body.appendChild(overlay);

        // Remove after 3 seconds
        setTimeout(() => {
            overlay.remove();
        }, 3000);
    }

    // Handle results after question
    handleResults(data) {
        console.log('Haunting race results:', data);

        const resultsData = data.results || data.data;

        // Hide question section
        const elements = this.getElements();
        if (elements.questionSection) {
            elements.questionSection.style.display = 'none';
        }

        // Show results
        if (elements.resultsSection) {
            elements.resultsSection.style.display = 'block';
            this.displayResults(resultsData);
        }

        // Update positions
        if (resultsData && resultsData.positions) {
            this.positions = resultsData.positions;
            this.updatePlayerPositions(true);
        }
    }

    // Display results
    displayResults(resultsData) {
        const elements = this.getElements();
        if (!elements.resultsSection) return;

        let html = '<div class="results-header">Question Results</div>';

        // Show question and correct answers
        if (resultsData.question_text) {
            html += `<div style="font-weight: 600; margin: 15px 0 10px 0; color: #333;">${resultsData.question_text}</div>`;
        }

        // Show statements with correct answers
        if (resultsData.statements) {
            html += '<div style="margin: 10px 0;">';
            resultsData.statements.forEach(stmt => {
                const answerIcon = stmt.is_true ? '✓' : '✗';
                const answerColor = stmt.is_true ? '#4CAF50' : '#f44336';
                const ghostBadge = stmt.is_ghost_only ? ' <span style="font-size: 0.8em;">👻</span>' : '';

                html += `
                    <div style="padding: 8px; margin: 5px 0; background: white; border-radius: 5px; border-left: 3px solid ${answerColor};">
                        <span style="color: ${answerColor}; font-weight: 700; margin-right: 8px;">${answerIcon}</span>
                        <span style="color: #333;">${stmt.text}</span>
                        ${ghostBadge}
                        <span style="float: right; color: ${answerColor}; font-weight: 600;">${stmt.is_true ? 'TRUE' : 'FALSE'}</span>
                    </div>
                `;
            });
            html += '</div>';
        }

        // Show movements (only on mobile, not on TV)
        if (resultsData.movements && !this.isTV) {
            html += '<div style="margin-top: 20px; padding-top: 15px; border-top: 2px solid #e0e0e0;">';
            html += '<div style="font-weight: 600; margin-bottom: 10px; color: #333;">Player Movement</div>';

            Object.keys(resultsData.movements).forEach(playerId => {
                const movement = resultsData.movements[playerId];
                const player = this.raceData.players.find(p => p.id == playerId);
                const playerName = player ? player.name : `Player ${playerId}`;
                const icon = playerId == this.raceData.unicorn_id ? '🦄' : '👻';

                html += `
                    <div class="player-result ${movement > 0 ? 'moved' : ''}">
                        <span>${icon} ${playerName}</span>
                        <span>+${movement} spaces</span>
                    </div>
                `;
            });
            html += '</div>';
        }

        elements.resultsSection.innerHTML = html;
    }

    // Handle race end
    handleRaceEnd(data) {
        console.log('Haunting race ended:', data);

        const winnerData = data.data;

        // Clear timer
        if (this.timerInterval) {
            clearInterval(this.timerInterval);
            this.timerInterval = null;
        }

        // Show winner screen
        this.showWinnerScreen(winnerData);

        // Mark race as inactive
        this.isActive = false;
    }

    // Show winner screen
    showWinnerScreen(winnerData) {
        const winner = this.raceData.players.find(p => p.id == winnerData.winner_id);
        const winnerName = winner ? winner.name : 'Player';

        // Create winner overlay
        const winnerScreen = document.createElement('div');
        winnerScreen.className = 'haunting-race-winner';

        const content = document.createElement('div');
        content.className = 'winner-content';

        const icon = document.createElement('div');
        icon.className = 'winner-icon';
        icon.textContent = '🦄';

        const title = document.createElement('div');
        title.className = 'winner-title';
        title.textContent = 'Victory!';

        const name = document.createElement('div');
        name.className = 'winner-name';
        name.textContent = winnerName;

        const message = document.createElement('div');
        message.style.cssText = 'font-size: 1.2rem; margin-top: 20px; opacity: 0.9;';
        message.textContent = 'The unicorn reached the finish line!';

        content.appendChild(icon);
        content.appendChild(title);
        content.appendChild(name);
        content.appendChild(message);
        winnerScreen.appendChild(content);

        document.body.appendChild(winnerScreen);

        // Remove after 5 seconds and return to normal game flow
        setTimeout(() => {
            winnerScreen.remove();
            this.cleanup();
        }, 5000);
    }

    // Show notification
    showNotification(message, type = 'info') {
        // Use existing notification system if available
        if (window.UI && window.UI.showNotification) {
            window.UI.showNotification(message, type);
        } else {
            console.log(`[${type.toUpperCase()}] ${message}`);
        }
    }

    // Cleanup
    cleanup() {
        // Clear timer
        if (this.timerInterval) {
            clearInterval(this.timerInterval);
            this.timerInterval = null;
        }

        // Hide race screen
        const elements = this.getElements();
        if (elements.screen) {
            elements.screen.classList.remove('active');
            elements.screen.classList.add('hidden');
        }

        // Reset state
        this.isActive = false;
        this.raceData = null;
        this.currentQuestion = null;
        this.selectedStatements.clear();
        this.hasAnswered = false;
        this.positions = {};
        this.isUnicorn = false;
    }

    // Destroy manager
    destroy() {
        this.cleanup();
        this.unregisterEventListeners();
    }
}

// Export for use in other files
if (typeof window !== 'undefined') {
    window.HauntingRaceManager = HauntingRaceManager;
}
