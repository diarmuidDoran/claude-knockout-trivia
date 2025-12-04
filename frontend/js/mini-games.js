/**
 * Mini-Games UI Manager
 * Handles the display and interaction for mini-games (Chalices and Worst Answer)
 */

class MiniGamesManager {
    constructor(websocketManager) {
        this.ws = websocketManager;
        this.currentGame = null;
        this.playerRole = null;
        this.gameData = null;
        this.playerId = null;
        this.timerInterval = null;  // Store timer reference for cleanup
        this.patternPhaseTimeout = null;  // Store Pattern Tiles phase transition timeout

        // Bind WebSocket event handlers
        this.setupEventHandlers();
    }

    setupEventHandlers() {
        // Listen for mini-game events
        if (this.ws) {
            this.ws.on('mini_game_start', this.handleMiniGameStart.bind(this));
            this.ws.on('mini_game_player_action', this.handlePlayerAction.bind(this));
            this.ws.on('mini_game_results', this.handleResults.bind(this));
            this.ws.on('mini_game_timeout', this.handleTimeout.bind(this));
            this.ws.on('mini_game_phase_change', this.handlePhaseChange.bind(this));
        }
    }

    handlePhaseChange(data) {
        console.log('[MINI-GAME] Phase change received:', data);
        console.log('[MINI-GAME] Game name:', data.game_name);
        console.log('[MINI-GAME] Phase:', data.phase);
        console.log('[MINI-GAME] Submitted answers:', data.submitted_answers);

        // Handle Worst Answer voting phase
        if (data.game_name === 'Worst Answer' && data.phase === 'voting') {
            console.log('[MINI-GAME] Transitioning to voting phase');
            this.showWorstAnswerVoting({
                question: data.question,
                submitted_answers: data.submitted_answers,
                at_risk_players: data.at_risk_players,
                safe_players: data.safe_players
            });
            // Start the voting timer (30 seconds)
            this.startTimer(30);
        }
    }

    setPlayerId(playerId) {
        console.log('[MINI-GAME] setPlayerId called with:', playerId, 'type:', typeof playerId);
        this.playerId = playerId;
    }

    // ========== MINI-GAME START ==========

    handleMiniGameStart(data) {
        console.log('[MINI-GAME] Starting:', data);
        this.currentGame = data.game_name;
        this.gameData = data.setup;

        // Determine player role
        this.determinePlayerRole(data.setup);

        // Show mini-game UI
        this.showMiniGameIntro(data);

        // Start timer
        this.startTimer(data.timeout || 45);

        // Show game-specific UI after intro
        setTimeout(() => {
            console.log('[MINI-GAME] Intro complete, showing game UI for:', this.currentGame);
            if (this.currentGame === 'Chalices') {
                this.showChalicesUI(data.setup);
            } else if (this.currentGame === 'Worst Answer') {
                this.showWorstAnswerUI(data.setup);
            } else if (this.currentGame === 'Quick Math') {
                console.log('[MINI-GAME] Calling showQuickMathUI with setup:', data.setup);
                this.showQuickMathUI(data.setup);
            } else if (this.currentGame === 'Grab More Points') {
                this.showGrabMorePointsUI(data.setup);
            } else if (this.currentGame === 'Pattern Tiles') {
                this.showPatternTilesUI(data.setup);
            } else if (this.currentGame === 'Playing at a Disadvantage') {
                this.showPlayingAtDisadvantageUI(data.setup);
            }
        }, 3000);  // 3 second intro
    }

    determinePlayerRole(setup) {
        const atRiskPlayers = setup.at_risk_players || [];
        const safePlayers = setup.safe_players || [];

        if (atRiskPlayers.includes(this.playerId)) {
            this.playerRole = 'at_risk';
        } else if (safePlayers.includes(this.playerId)) {
            this.playerRole = 'safe';
        } else {
            this.playerRole = 'ghost';
        }

        console.log(`[MINI-GAME] Player role: ${this.playerRole}`);
    }

    showMiniGameIntro(data) {
        const container = document.getElementById('mini-game-container');
        if (!container) {
            console.error('[MINI-GAME] Container not found');
            return;
        }

        // Hide question and result containers when showing mini-game
        const questionContainer = document.getElementById('question-container');
        const resultContainer = document.getElementById('result-container');
        const waitingQuestion = document.getElementById('waiting-question');

        if (questionContainer) questionContainer.classList.add('hidden');
        if (resultContainer) resultContainer.classList.add('hidden');
        if (waitingQuestion) waitingQuestion.classList.add('hidden');

        container.innerHTML = `
            <div class="mini-game-intro">
                <h1 class="mini-game-title">${data.game_name}</h1>
                <p class="mini-game-description">${data.description}</p>
                <div class="mini-game-role">
                    <h3>Your Role: ${this.getRoleDisplay()}</h3>
                    <p>${this.getRoleDescription(data.setup)}</p>
                </div>
                <div class="mini-game-timer">
                    Starting in <span id="intro-countdown">3</span>...
                </div>
            </div>
        `;

        container.style.display = 'block';

        // Countdown
        let count = 3;
        const countdown = setInterval(() => {
            count--;
            const countdownEl = document.getElementById('intro-countdown');
            if (countdownEl) {
                if (count > 0) {
                    countdownEl.textContent = count;
                } else {
                    clearInterval(countdown);
                }
            }
        }, 1000);
    }

    getRoleDisplay() {
        // For Quick Math, show Racer or Observer
        if (this.currentGame === 'Quick Math') {
            const racers = this.gameData?.racers || [];
            const isRacer = racers.includes(this.playerId) || racers.includes(parseInt(this.playerId));
            return isRacer ? '🏃 Racer' : '👀 Observer';
        }

        // For other games, use standard roles
        switch (this.playerRole) {
            case 'at_risk': return '⚠️ At Risk';
            case 'safe': return '✅ Safe';
            case 'ghost': return '👻 Ghost';
            default: return 'Observer';
        }
    }

    getRoleDescription(setup) {
        const roles = setup.roles || {};

        // For Quick Math, determine if player is a racer or observer
        if (this.currentGame === 'Quick Math') {
            const racers = setup.racers || [];
            const isRacer = racers.includes(this.playerId) || racers.includes(parseInt(this.playerId));
            const quickMathRole = isRacer ? 'racer' : 'observer';
            const roleData = roles[quickMathRole];
            return roleData ? roleData.description : 'Watch the race unfold!';
        }

        // For other games, use the standard player role
        const roleData = roles[this.playerRole];
        return roleData ? roleData.description : 'Watch the game unfold!';
    }

    startTimer(seconds) {
        const timerEl = document.getElementById('mini-game-timer-display');
        if (!timerEl) return;

        // Clear any existing timer
        if (this.timerInterval) {
            clearInterval(this.timerInterval);
            this.timerInterval = null;
        }

        let remaining = seconds;
        timerEl.textContent = remaining;

        this.timerInterval = setInterval(() => {
            remaining--;
            if (timerEl) {
                timerEl.textContent = remaining;

                if (remaining <= 10) {
                    timerEl.classList.add('timer-warning');
                }
                if (remaining <= 0) {
                    clearInterval(this.timerInterval);
                    this.timerInterval = null;
                    timerEl.textContent = "Time's up!";
                }
            } else {
                clearInterval(this.timerInterval);
                this.timerInterval = null;
            }
        }, 1000);
    }

    stopTimer() {
        if (this.timerInterval) {
            clearInterval(this.timerInterval);
            this.timerInterval = null;
        }
    }

    // ========== CHALICES MINI-GAME ==========

    showChalicesUI(setup) {
        const container = document.getElementById('mini-game-container');
        if (!container) return;

        const numChalices = setup.num_chalices || 3;
        const role = this.playerRole;

        let html = `
            <div class="chalices-game">
                <h2>🍷 Chalices Game</h2>
                <p class="timer-display">Time remaining: <span id="mini-game-timer-display">30</span>s</p>

                <div class="chalices-container">
        `;

        // Show chalices
        for (let i = 0; i < numChalices; i++) {
            html += `
                <div class="chalice" data-chalice="${i}">
                    <div class="chalice-icon">🍷</div>
                    <div class="chalice-label">Chalice ${i + 1}</div>
                </div>
            `;
        }

        html += `</div>`;

        // Role-specific UI - NO SUBMIT BUTTON, click to lock
        if (role === 'safe') {
            // Poisoner - click a chalice to poison it (locked on click)
            html += `
                <div class="action-panel poisoner-panel">
                    <h3>⚗️ Poison a Chalice</h3>
                    <p>Click a chalice to poison it. Your choice is locked!</p>
                    <p class="selection-info" id="selection-info">Click a chalice to poison it</p>
                </div>
            `;
        } else if (role === 'at_risk') {
            // Tester - click a chalice to drink from (locked on click)
            html += `
                <div class="action-panel tester-panel">
                    <h3>🎯 Choose Your Chalice</h3>
                    <p>Click a chalice to drink from it. Choose wisely - no changing!</p>
                    <p class="selection-info" id="selection-info">Click a chalice to drink from it</p>
                </div>
            `;
        } else {
            html += `
                <div class="action-panel observer-panel">
                    <h3>👻 Observing</h3>
                    <p>Watch as the game unfolds...</p>
                </div>
            `;
        }

        html += `</div>`;
        container.innerHTML = html;

        // Track if player has locked in their choice
        this.chalicesLocked = false;

        // Add click handlers
        this.setupChalicesHandlers(setup);
    }

    setupChalicesHandlers(setup) {
        const chalices = document.querySelectorAll('.chalice');
        const selectionInfo = document.getElementById('selection-info');

        chalices.forEach(chalice => {
            chalice.addEventListener('click', () => {
                // Don't allow clicks if already locked or ghost
                if (this.chalicesLocked || this.playerRole === 'ghost') {
                    return;
                }

                const chaliceNum = parseInt(chalice.dataset.chalice);

                if (this.playerRole === 'at_risk') {
                    // Tester: single selection, immediately locked
                    this.chalicesLocked = true;

                    // Visual feedback
                    chalices.forEach(c => {
                        c.classList.remove('selected');
                        c.classList.add('disabled');
                    });
                    chalice.classList.add('selected', 'locked');
                    chalice.classList.remove('disabled');

                    // Show confirmation
                    if (selectionInfo) {
                        selectionInfo.innerHTML = `<span class="locked-indicator">🔒</span> You will drink from Chalice ${chaliceNum + 1}`;
                        selectionInfo.classList.add('choice-locked');
                    }

                    // Submit immediately
                    this.submitChalicesAction('choose_chalice', chaliceNum);

                } else if (this.playerRole === 'safe') {
                    // Poisoner: single selection, immediately locked
                    this.chalicesLocked = true;

                    // Visual feedback
                    chalices.forEach(c => {
                        c.classList.remove('selected');
                        c.classList.add('disabled');
                    });
                    chalice.classList.add('selected', 'locked', 'poisoned');
                    chalice.classList.remove('disabled');

                    // Show confirmation
                    if (selectionInfo) {
                        selectionInfo.innerHTML = `<span class="locked-indicator">🔒</span> You poisoned Chalice ${chaliceNum + 1}`;
                        selectionInfo.classList.add('choice-locked');
                    }

                    // Submit immediately
                    this.submitChalicesAction('poison_chalice', chaliceNum);
                }
            });
        });
    }

    submitChalicesAction(actionType, chalice) {
        const action = { type: actionType, chalice: chalice };

        console.log('[MINI-GAME] Submitting Chalices action:', action);
        console.log('[MINI-GAME] Chalice value:', chalice, 'type:', typeof chalice);
        this.ws.send({
            type: 'mini_game_action',
            action: action
        });
    }

    // ========== WORST ANSWER MINI-GAME ==========

    showWorstAnswerUI(setup) {
        const container = document.getElementById('mini-game-container');
        if (!container) return;

        const phase = setup.phase || 'submission';
        const question = setup.question || 'What is the worst...?';

        if (phase === 'submission') {
            this.showWorstAnswerSubmission(question, setup);
        } else if (phase === 'voting') {
            this.showWorstAnswerVoting(setup);
        }
    }

    showWorstAnswerSubmission(question, setup) {
        const container = document.getElementById('mini-game-container');

        let html = `
            <div class="worst-answer-game">
                <h2>💭 Worst Answer</h2>
                <p class="timer-display">Time remaining: <span id="mini-game-timer-display">30</span>s</p>

                <div class="question-display">
                    <h3>${question}</h3>
                </div>
        `;

        if (this.playerRole === 'at_risk') {
            html += `
                <div class="action-panel submission-panel">
                    <h3>✍️ Submit Your Answer</h3>
                    <p>Submit what you think is the WORST answer:</p>
                    <input type="text" id="answer-input" class="answer-input" maxlength="30" placeholder="Type your answer...">
                    <p class="char-count"><span id="char-count">0</span>/30 characters</p>
                    <button id="answer-submit-btn" class="action-button" disabled>
                        Submit Answer
                    </button>
                </div>
            `;
        } else {
            html += `
                <div class="action-panel waiting-panel">
                    <h3>⏳ Waiting for Answers</h3>
                    <p>Players are submitting their worst answers...</p>
                </div>
            `;
        }

        html += `</div>`;
        container.innerHTML = html;

        // Setup handlers
        this.setupWorstAnswerSubmissionHandlers();
    }

    setupWorstAnswerSubmissionHandlers() {
        const input = document.getElementById('answer-input');
        const submitBtn = document.getElementById('answer-submit-btn');
        const charCount = document.getElementById('char-count');

        if (!input || !submitBtn) return;

        input.addEventListener('input', () => {
            const length = input.value.length;
            charCount.textContent = length;
            submitBtn.disabled = length === 0 || length > 30;
        });

        submitBtn.addEventListener('click', () => {
            const answer = input.value.trim();
            if (answer.length > 0 && answer.length <= 30) {
                this.submitWorstAnswer(answer);
                submitBtn.disabled = true;
                input.disabled = true;
                submitBtn.textContent = 'Submitted! ✓';
            }
        });
    }

    submitWorstAnswer(answer) {
        console.log('[MINI-GAME] Submitting answer:', answer);
        this.ws.send({
            type: 'mini_game_action',
            action: {
                type: 'submit_answer',
                answer: answer
            }
        });
    }

    showWorstAnswerVoting(setup) {
        const container = document.getElementById('mini-game-container');
        if (!container) {
            console.error('[MINI-GAME] Container not found for voting');
            return;
        }

        const submittedAnswers = setup.submitted_answers || {};
        console.log('[MINI-GAME] Showing voting UI with answers:', submittedAnswers);
        console.log('[MINI-GAME] Question:', setup.question);
        console.log('[MINI-GAME] My player ID:', this.playerId);

        // Hide question and result containers when showing voting
        const questionContainer = document.getElementById('question-container');
        const resultContainer = document.getElementById('result-container');
        const waitingQuestion = document.getElementById('waiting-question');

        if (questionContainer) questionContainer.classList.add('hidden');
        if (resultContainer) resultContainer.classList.add('hidden');
        if (waitingQuestion) waitingQuestion.classList.add('hidden');

        let html = `
            <div class="worst-answer-game">
                <h2>💭 Worst Answer - Voting</h2>
                <p class="timer-display">Time remaining: <span id="mini-game-timer-display">30</span>s</p>

                <div class="question-display">
                    <h3>${setup.question || 'Vote for the worst answer!'}</h3>
                </div>

                <div class="action-panel voting-panel">
                    <h3>🗳️ Vote for the Worst Answer</h3>
                    <p>Click on the answer you think is the worst:</p>
                    <div class="answers-list">
        `;

        // Show all submitted answers
        for (const [playerId, answer] of Object.entries(submittedAnswers)) {
            const isOwnAnswer = parseInt(playerId) === this.playerId;
            console.log(`[MINI-GAME] Answer from player ${playerId}: "${answer}" (isOwn: ${isOwnAnswer})`);
            html += `
                <div class="answer-option ${isOwnAnswer ? 'own-answer' : ''}" data-player-id="${playerId}">
                    <div class="answer-text">${answer}</div>
                    ${isOwnAnswer ? '<span class="own-badge">Your Answer</span>' : ''}
                </div>
            `;
        }

        html += `
                    </div>
                    <button id="vote-submit-btn" class="action-button" disabled>
                        Submit Vote
                    </button>
                    <p class="selection-info" id="selection-info">Select an answer to vote</p>
                </div>
            </div>
        `;

        container.innerHTML = html;

        // Make sure container is visible
        container.style.display = 'block';

        // Setup voting handlers
        this.setupWorstAnswerVotingHandlers();
    }

    setupWorstAnswerVotingHandlers() {
        const answers = document.querySelectorAll('.answer-option:not(.own-answer)');
        const submitBtn = document.getElementById('vote-submit-btn');
        const selectionInfo = document.getElementById('selection-info');
        let selectedPlayerId = null;

        answers.forEach(answer => {
            answer.addEventListener('click', () => {
                // Remove previous selection
                answers.forEach(a => a.classList.remove('selected'));

                // Select this answer
                answer.classList.add('selected');
                selectedPlayerId = parseInt(answer.dataset.playerId);

                submitBtn.disabled = false;
                selectionInfo.textContent = 'Answer selected!';
            });
        });

        if (submitBtn) {
            submitBtn.addEventListener('click', () => {
                if (selectedPlayerId !== null) {
                    this.submitVote(selectedPlayerId);
                    submitBtn.disabled = true;
                    submitBtn.textContent = 'Voted! ✓';
                }
            });
        }
    }

    submitVote(votedFor) {
        console.log('[MINI-GAME] Submitting vote for player:', votedFor);
        this.ws.send({
            type: 'mini_game_action',
            action: {
                type: 'vote',
                voted_for: votedFor
            }
        });
    }

    // ========== EVENT HANDLERS ==========

    handlePlayerAction(data) {
        console.log('[MINI-GAME] Player action received:', data);
        // Update UI to show that a player has acted
        const info = document.getElementById('selection-info');
        if (info) {
            info.textContent = 'Other players are making their choices...';
        }
    }

    handleResults(data) {
        console.log('[MINI-GAME] Results:', data);
        // Stop the timer immediately when results arrive
        this.stopTimer();

        // Clear Pattern Tiles phase timeout if it exists
        if (this.patternPhaseTimeout) {
            console.log('[MINI-GAME] Clearing Pattern Tiles phase timeout on results');
            clearTimeout(this.patternPhaseTimeout);
            this.patternPhaseTimeout = null;
        }

        this.showResults(data);
    }

    handleTimeout(data) {
        console.log('[MINI-GAME] Timeout:', data);
        // Stop the timer
        this.stopTimer();
        const container = document.getElementById('mini-game-container');
        if (container) {
            container.innerHTML = `
                <div class="mini-game-timeout">
                    <h2>⏰ Time's Up!</h2>
                    <p>${data.message}</p>
                </div>
            `;
        }
    }

    showResults(data) {
        const container = document.getElementById('mini-game-container');
        if (!container) return;

        const eliminated = data.eliminated || [];
        const gameData = data.game_data || {};

        let html = `
            <div class="mini-game-results">
                <h2>📊 Results</h2>
        `;

        // Show eliminated players
        if (eliminated.length > 0) {
            html += `<div class="eliminated-players">`;
            eliminated.forEach(player => {
                html += `
                    <div class="eliminated-player">
                        <span class="ghost-icon">👻</span>
                        <span class="player-name">${player.player_name}</span>
                        <span class="elimination-label">Eliminated</span>
                    </div>
                `;
            });
            html += `</div>`;
        } else {
            html += `<p class="no-eliminations">No one was eliminated this round!</p>`;
        }

        // Show game-specific data
        if (this.currentGame === 'Chalices' && gameData.poisoned_chalices) {
            html += `
                <div class="game-details">
                    <h3>Poisoned Chalices:</h3>
                    <p>${Array.from(gameData.poisoned_chalices).map(c => `Chalice ${c + 1}`).join(', ')}</p>
                </div>
            `;
        } else if (this.currentGame === 'Worst Answer' && gameData.vote_counts) {
            html += `
                <div class="game-details">
                    <h3>Vote Counts:</h3>
                    <ul class="vote-list">
            `;
            for (const [playerId, votes] of Object.entries(gameData.vote_counts)) {
                html += `<li>Player: ${votes} votes</li>`;
            }
            html += `
                    </ul>
                </div>
            `;
        }

        html += `
                <p class="next-round-notice">Next question starting soon...</p>
            </div>
        `;

        container.innerHTML = html;

        console.log('[MINI-GAME] Results displayed, will hide container after 5 seconds');

        // Hide after 5 seconds (but next_question event may hide it sooner)
        setTimeout(() => {
            console.log('[MINI-GAME] 5 seconds elapsed, hiding results container');
            container.style.display = 'none';
            this.currentGame = null;
            this.playerRole = null;
            this.gameData = null;
        }, 5000);
    }

    // ========== QUICK MATH MINI-GAME ==========

    showQuickMathUI(setup) {
        console.log('[QUICK-MATH] ===== showQuickMathUI called =====');
        const container = document.getElementById('mini-game-container');
        if (!container) {
            console.error('[QUICK-MATH] Container not found!');
            return;
        }

        const gameMode = setup.game_mode || 'at_risk_vs_at_risk';
        const racers = setup.racers || [];

        // Debug logging
        console.log('[QUICK-MATH] Setup received:', setup);
        console.log('[QUICK-MATH] Racers:', racers);
        console.log('[QUICK-MATH] My player ID:', this.playerId, 'type:', typeof this.playerId);

        // Check if player is a racer (handle potential type mismatch)
        const isRacer = racers.includes(this.playerId) || racers.includes(parseInt(this.playerId));
        console.log('[QUICK-MATH] Is racer:', isRacer);

        // Pre-generate first question for racers
        let firstQuestion = null;
        if (isRacer) {
            this.currentQuestionId = 1;
            firstQuestion = this.generateMathQuestion();
            this.currentQuestion = firstQuestion;
            console.log('[QUICK-MATH] Pre-generated first question:', firstQuestion);
        } else {
            console.log('[QUICK-MATH] Player is observer, no question generation');
        }

        // No timer on mobile - timer shown on TV only
        let html = `
            <div class="quick-math-game">
                <h2>🧮 Quick Math Race</h2>
                <p class="score-display">Your Score: <span id="player-score">0</span></p>
        `;

        if (isRacer) {
            // Show first question directly in HTML
            const questionDisplay = firstQuestion ? `${firstQuestion.question} = ?` : 'Loading...';
            console.log('[QUICK-MATH] Question display text:', questionDisplay);
            html += `
                <div class="math-question-container">
                    <div id="math-question" class="math-question">
                        <span class="math-question-text" id="math-question-text">${questionDisplay}</span>
                    </div>
                    <div class="answer-input-container">
                        <input type="number" id="math-answer-input" class="math-answer-input"
                               placeholder="?" autocomplete="off" inputmode="numeric" pattern="[0-9]*">
                        <button id="submit-answer-btn" class="submit-answer-btn">
                            Submit
                        </button>
                    </div>
                    <div class="feedback" id="answer-feedback"></div>
                </div>

                <div class="instructions">
                    <p>Answer as many as you can!</p>
                    <p class="game-mode-info">${this.getQuickMathModeDescription(gameMode, setup)}</p>
                </div>
            `;
        } else {
            html += `
                <div class="observer-panel">
                    <h3>👀 Spectating</h3>
                    <p>Watch the race on the TV!</p>
                </div>
            `;
        }

        html += `</div>`;
        container.innerHTML = html;
        console.log('[QUICK-MATH] HTML set to container');

        // Ensure container is visible
        container.style.display = 'block';

        // Verify the question text element exists
        const questionTextEl = document.getElementById('math-question-text');
        console.log('[QUICK-MATH] Question text element:', questionTextEl);
        console.log('[QUICK-MATH] Question text content:', questionTextEl?.textContent);

        if (isRacer) {
            console.log('[QUICK-MATH] Player is a racer, setting up handlers');
            this.mathScore = 0;
            this.setupQuickMathHandlers();

            // Focus the input after a short delay to ensure DOM is ready
            setTimeout(() => {
                const input = document.getElementById('math-answer-input');
                if (input) {
                    input.focus();
                    console.log('[QUICK-MATH] Input focused, ready for answers');
                }
            }, 100);
        } else {
            console.log('[QUICK-MATH] Player is NOT a racer, showing observer UI');
        }
    }

    getQuickMathModeDescription(gameMode, setup) {
        if (gameMode === 'at_risk_vs_at_risk') {
            return `⚠️ ${setup.at_risk_players.length} at-risk players competing. Lowest score is eliminated!`;
        } else {
            return `🎯 At-risk player must place 1st to survive!`;
        }
    }

    setupQuickMathHandlers() {
        const input = document.getElementById('math-answer-input');
        const submitBtn = document.getElementById('submit-answer-btn');

        console.log('[QUICK-MATH] setupQuickMathHandlers called');
        console.log('[QUICK-MATH] Elements found - input:', !!input, 'submitBtn:', !!submitBtn);

        if (!input || !submitBtn) {
            console.error('[QUICK-MATH] Could not find input or submit button elements!');
            return;
        }

        // Don't reset question state if already set (first question is pre-generated)
        // Only initialize if not already set
        if (!this.currentQuestion) {
            console.log('[QUICK-MATH] No current question set, initializing state');
            this.currentQuestion = null;
            this.currentQuestionId = 0;
        } else {
            console.log('[QUICK-MATH] Current question already set:', this.currentQuestion);
        }

        // Handle Enter key
        input.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                e.preventDefault();
                this.submitMathAnswer();
            }
        });

        // Handle submit button
        submitBtn.addEventListener('click', () => {
            this.submitMathAnswer();
        });

        console.log('[QUICK-MATH] Handlers attached successfully');
    }

    // Generate math question client-side for instant responsiveness
    // Requirements: all numbers ≤ 2 digits (≤99), whole numbers only
    generateMathQuestion() {
        const operations = ['+', '-', '×', '÷'];
        const operation = operations[Math.floor(Math.random() * operations.length)];

        let a, b, answer, question;

        if (operation === '+') {
            // Addition: result must be ≤ 99
            a = Math.floor(Math.random() * 50) + 1;  // 1-50
            b = Math.floor(Math.random() * Math.min(99 - a, 50)) + 1;  // Ensure sum ≤ 99
            answer = a + b;
            question = `${a} + ${b}`;
        } else if (operation === '-') {
            // Subtraction: both numbers ≤ 99, result positive
            a = Math.floor(Math.random() * 89) + 10;  // 10-98
            b = Math.floor(Math.random() * (a - 1)) + 1;  // 1 to (a-1), ensure positive result
            answer = a - b;
            question = `${a} - ${b}`;
        } else if (operation === '×') {
            // Multiplication: both operands ≤ 2 digits
            // Limit to smaller numbers to keep mental math reasonable
            a = Math.floor(Math.random() * 12) + 1;  // 1-12
            b = Math.floor(Math.random() * 12) + 1;  // 1-12
            answer = a * b;
            question = `${a} × ${b}`;
        } else {  // Division
            // Division: dividend must be ≤ 99, whole number answer
            // Pick quotient and divisor such that quotient × divisor ≤ 99
            const quotient = Math.floor(Math.random() * 12) + 1;  // 1-12
            const maxDivisor = Math.floor(99 / quotient);  // Ensure dividend ≤ 99
            const divisor = Math.floor(Math.random() * Math.min(maxDivisor - 1, 11)) + 2;  // 2 to min(maxDivisor, 12)
            a = divisor * quotient;  // dividend, always ≤ 99
            b = divisor;
            answer = quotient;
            question = `${a} ÷ ${b}`;
        }

        return {
            question_id: this.currentQuestionId,
            question: question,
            answer: answer
        };
    }

    generateAndShowMathQuestion() {
        console.log('[QUICK-MATH] generateAndShowMathQuestion called');

        try {
            this.currentQuestionId++;
            this.currentQuestion = this.generateMathQuestion();
            console.log('[QUICK-MATH] Generated question:', this.currentQuestion);

            const questionText = document.getElementById('math-question-text');
            const input = document.getElementById('math-answer-input');
            const feedback = document.getElementById('answer-feedback');

            console.log('[QUICK-MATH] Elements found - questionText:', !!questionText, 'input:', !!input);

            if (questionText) {
                questionText.textContent = this.currentQuestion.question + ' = ?';
                questionText.classList.add('pulse-animation');
                setTimeout(() => questionText.classList.remove('pulse-animation'), 300);
                console.log('[QUICK-MATH] Question text updated to:', questionText.textContent);
            } else {
                console.error('[QUICK-MATH] Could not find math-question-text element!');
            }

            if (input) {
                input.value = '';
                input.focus();
            }

            if (feedback) {
                feedback.textContent = '';
                feedback.className = 'feedback';
            }

            console.log('[QUICK-MATH] New question displayed:', this.currentQuestion.question);
        } catch (error) {
            console.error('[QUICK-MATH] Error generating question:', error);
        }
    }

    submitMathAnswer() {
        const input = document.getElementById('math-answer-input');
        const feedback = document.getElementById('answer-feedback');
        const scoreEl = document.getElementById('player-score');

        if (!input || !this.currentQuestion) return;

        const answer = input.value.trim();
        if (answer === '') return;

        // Check answer locally
        const isCorrect = parseInt(answer) === this.currentQuestion.answer;
        console.log('[QUICK-MATH] Answer submitted:', answer, 'Expected:', this.currentQuestion.answer, 'Correct:', isCorrect);

        if (isCorrect) {
            this.mathScore++;
            console.log('[QUICK-MATH] Score incremented to:', this.mathScore);

            // Send score update to server
            this.ws.send({
                type: 'mini_game_action',
                action: {
                    type: 'answer',
                    question_id: this.currentQuestionId,
                    answer: parseInt(answer),
                    is_correct: true
                }
            });

            if (feedback) {
                feedback.textContent = '✓ Correct!';
                feedback.className = 'feedback correct';
            }

            // Update score display
            if (scoreEl) {
                console.log('[QUICK-MATH] Updating score element, old text:', scoreEl.textContent, 'new score:', this.mathScore);
                scoreEl.textContent = this.mathScore;
                console.log('[QUICK-MATH] Score element updated, new text:', scoreEl.textContent);
                scoreEl.classList.add('score-increase');
                setTimeout(() => scoreEl.classList.remove('score-increase'), 300);

                // Verify the element is still in the DOM
                const verification = document.getElementById('player-score');
                console.log('[QUICK-MATH] Verification check - element still exists:', !!verification, 'text:', verification?.textContent);
            } else {
                console.error('[QUICK-MATH] Score element not found!');
            }
        } else {
            if (feedback) {
                feedback.textContent = `✗ Wrong! (${this.currentQuestion.answer})`;
                feedback.className = 'feedback incorrect';
            }
        }

        // Clear feedback after brief moment
        setTimeout(() => {
            if (feedback) {
                feedback.textContent = '';
                feedback.className = 'feedback';
            }
        }, 600);

        // Generate next question immediately for speed
        setTimeout(() => this.generateAndShowMathQuestion(), 100);
    }

    // ========== GRAB MORE POINTS MINI-GAME ==========

    showGrabMorePointsUI(setup) {
        const container = document.getElementById('mini-game-container');
        if (!container) return;

        const atRiskPlayers = setup.at_risk_players || [];
        const isAtRisk = atRiskPlayers.includes(this.playerId);
        const rules = setup.rules || {};

        let html = `
            <div class="grab-more-points-game">
                <h2>💰 Grab More Points</h2>
                <p class="timer-display">Time remaining: <span id="mini-game-timer-display">30</span>s</p>
        `;

        // Show rules
        html += `
            <div class="game-rules-box">
                <h3>${rules.title || 'The Rules'}</h3>
                <div class="rules-section">
                    <h4>How It Works:</h4>
                    <ul class="rules-list">
                        ${(rules.main_rules || []).map(rule => `<li>${rule}</li>`).join('')}
                    </ul>
                </div>
                <div class="rules-section outcomes">
                    <h4>Possible Outcomes:</h4>
                    <ul class="outcomes-list">
                        ${(rules.outcomes || []).map(outcome => `<li>${outcome}</li>`).join('')}
                    </ul>
                </div>
                <div class="strategy-hint">
                    <em>${rules.strategy || 'Choose wisely!'}</em>
                </div>
            </div>
        `;

        if (isAtRisk) {
            // At-risk player - show decision form
            html += `
                <div class="points-decision-container">
                    <h3>Your Decision:</h3>
                    <p class="decision-prompt">How many points do you want to grab?</p>

                    <div class="points-input-container">
                        <input type="number"
                               id="points-input"
                               class="points-input"
                               placeholder="0"
                               min="0"
                               max="1000"
                               autocomplete="off"
                               inputmode="numeric">
                        <span class="points-label">/ 1000</span>
                    </div>

                    <button id="submit-points-btn" class="submit-points-btn">
                        No points thanks
                    </button>

                    <div class="decision-feedback" id="decision-feedback"></div>
                </div>
            `;
        } else {
            // Observer - show waiting screen
            html += `
                <div class="observer-panel">
                    <h3>👀 Observing</h3>
                    <p>Watching the at-risk players make their decisions...</p>
                    <p class="suspense-text">What will they choose? 🤔</p>
                </div>
            `;
        }

        html += `</div>`;
        container.innerHTML = html;

        if (isAtRisk) {
            this.setupGrabMorePointsHandlers();
        }
    }

    setupGrabMorePointsHandlers() {
        const input = document.getElementById('points-input');
        const submitBtn = document.getElementById('submit-points-btn');

        if (!input || !submitBtn) return;

        // Auto-focus input
        input.focus();

        // Update button text based on input value
        const updateButtonText = () => {
            const value = parseInt(input.value) || 0;
            if (value === 0 || input.value === '') {
                submitBtn.textContent = 'No points thanks';
                submitBtn.className = 'submit-points-btn no-points';
            } else {
                submitBtn.textContent = 'Give me the points!';
                submitBtn.className = 'submit-points-btn take-points';
            }
        };

        // Listen for input changes
        input.addEventListener('input', updateButtonText);

        // Enforce max value
        input.addEventListener('input', () => {
            const value = parseInt(input.value) || 0;
            if (value > 1000) {
                input.value = 1000;
            }
            if (value < 0) {
                input.value = 0;
            }
        });

        // Handle Enter key
        input.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                e.preventDefault();
                this.submitPointsDecision();
            }
        });

        // Handle submit button
        submitBtn.addEventListener('click', () => {
            this.submitPointsDecision();
        });

        // Initial button state
        updateButtonText();
    }

    submitPointsDecision() {
        const input = document.getElementById('points-input');
        const submitBtn = document.getElementById('submit-points-btn');
        const feedback = document.getElementById('decision-feedback');

        if (!input) return;

        // Get points value (default to 0)
        const points = parseInt(input.value) || 0;

        // Validate
        if (points < 0 || points > 1000) {
            if (feedback) {
                feedback.textContent = 'Please enter a value between 0 and 1000';
                feedback.className = 'decision-feedback error';
            }
            return;
        }

        // Submit to server
        this.ws.send({
            type: 'mini_game_action',
            action: {
                type: 'submit_points',
                points: points
            }
        });

        // Disable form
        if (input) {
            input.disabled = true;
        }
        if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.textContent = points > 0 ? `Taking ${points} points...` : 'Taking no points...';
        }

        // Show confirmation
        if (feedback) {
            if (points > 0) {
                feedback.textContent = `✓ Submitted: Grabbing ${points} points!`;
                feedback.className = 'decision-feedback success greedy';
            } else {
                feedback.textContent = '✓ Submitted: Taking no points';
                feedback.className = 'decision-feedback success noble';
            }
        }

        console.log(`[GRAB-MORE-POINTS] Submitted decision: ${points} points`);
    }

    // ========== PATTERN TILES ==========

    showPatternTilesUI(setup) {
        const playersCompeting = setup.players_competing || [];
        const pattern = setup.pattern || [];
        const gameMode = setup.game_mode || '';
        const rules = setup.rules || {};

        // Debug logging
        console.log('[PATTERN-TILES] Setup received:', setup);
        console.log('[PATTERN-TILES] Players competing:', playersCompeting);
        console.log('[PATTERN-TILES] My player ID:', this.playerId, 'type:', typeof this.playerId);

        // Check if player is competing (handle potential type mismatch)
        const isCompeting = playersCompeting.includes(this.playerId) || playersCompeting.includes(parseInt(this.playerId));
        console.log('[PATTERN-TILES] Is competing:', isCompeting);

        const container = document.getElementById('mini-game-container');
        if (!container) return;

        // Clear any existing Pattern Tiles phase timeout from previous game
        if (this.patternPhaseTimeout) {
            console.log('[PATTERN-TILES] Clearing existing phase timeout from previous game');
            clearTimeout(this.patternPhaseTimeout);
            this.patternPhaseTimeout = null;
        }

        // Ensure container is visible
        container.style.display = 'block';

        // Start with memorization phase
        this.showPatternMemorizationPhase(pattern, rules, isCompeting, gameMode);

        // Transition to recreation phase after 10 seconds
        this.patternPhaseTimeout = setTimeout(() => {
            // Notify backend to transition phase
            this.ws.send({
                type: 'mini_game_action',
                action: {
                    type: 'start_recreation'
                }
            });
            console.log('[PATTERN-TILES] Sent start_recreation to backend');

            if (isCompeting) {
                console.log('[PATTERN-TILES] Showing recreation phase for competing player');
                this.showPatternRecreationPhase(pattern, rules, gameMode);
            } else {
                console.log('[PATTERN-TILES] Showing observer phase');
                this.showPatternObserverPhase(rules, gameMode);
            }

            // Clear timeout reference after it fires
            this.patternPhaseTimeout = null;
        }, 10000); // 10 seconds for memorization
    }

    showPatternMemorizationPhase(pattern, rules, isCompeting, gameMode) {
        const container = document.getElementById('mini-game-container');
        if (!container) return;

        let html = `
            <div class="pattern-tiles-game">
                <h2>🧩 Pattern Tiles - Memorization Phase</h2>
                <p class="phase-instruction">Study the pattern carefully! (Watch TV for timer)</p>

                <!-- Rules Box -->
                <div class="game-rules-box pattern-rules">
                    <h3>${rules.title || '🧩 Pattern Tiles - Memory Challenge'}</h3>
                    <div class="rules-section">
                        <h4>Phases:</h4>
                        <ul class="rules-list">
                            ${(rules.phases || []).map(phase => `<li>${phase}</li>`).join('')}
                        </ul>
                    </div>
                    <div class="rules-section">
                        <h4>Gameplay:</h4>
                        <ul class="rules-list">
                            ${(rules.gameplay || []).map(rule => `<li>${rule}</li>`).join('')}
                        </ul>
                    </div>
                    <div class="rules-section elimination">
                        <h4>Elimination:</h4>
                        <p class="elimination-rule">${rules.elimination || ''}</p>
                    </div>
                </div>

                <!-- Pattern Grid (TV Screen) -->
                <div class="pattern-display">
                    <h3>📺 Pattern to Memorize</h3>
                    <div class="tile-grid pattern-grid" id="pattern-grid">
                        ${this.renderTileGrid(pattern, false)}
                    </div>
                </div>

                ${!isCompeting ? `
                    <div class="observer-panel">
                        <p>👀 You are observing this mini-game</p>
                    </div>
                ` : `
                    <div class="player-instruction">
                        <p>💡 Your grid will appear in <span id="memorization-timer-2">10</span> seconds...</p>
                    </div>
                `}
            </div>
        `;

        container.innerHTML = html;

        // Countdown for memorization phase
        let timeLeft = 10;
        const timerInterval = setInterval(() => {
            timeLeft--;
            const timerEl = document.getElementById('memorization-timer');
            const timerEl2 = document.getElementById('memorization-timer-2');
            if (timerEl) timerEl.textContent = timeLeft;
            if (timerEl2) timerEl2.textContent = timeLeft;

            if (timeLeft <= 0) {
                clearInterval(timerInterval);
            }
        }, 1000);
    }

    showPatternRecreationPhase(pattern, rules, gameMode) {
        console.log('[PATTERN-TILES] showPatternRecreationPhase called');
        const container = document.getElementById('mini-game-container');
        if (!container) {
            console.error('[PATTERN-TILES] Container not found for recreation phase');
            return;
        }

        // Initialize player's grid (all white/0)
        this.playerGrid = Array(4).fill(null).map(() => Array(4).fill(0));
        console.log('[PATTERN-TILES] Initialized player grid:', this.playerGrid);

        let html = `
            <div class="pattern-tiles-game">
                <h2>🧩 Pattern Tiles - Recreation Phase</h2>
                <p class="phase-instruction">Recreate the pattern you just saw! (Watch TV for timer)</p>

                <!-- Player Grid (Interactive) -->
                <div class="player-grid-container">
                    <h3>Your Grid</h3>
                    <p class="grid-instruction">Click tiles to toggle between white and blue</p>
                    <div class="tile-grid player-grid" id="player-grid">
                        ${this.renderTileGrid(this.playerGrid, true)}
                    </div>
                </div>

                <!-- Submit Button -->
                <button id="submit-pattern-btn" class="submit-pattern-btn">
                    Submit Pattern
                </button>

                <div class="submission-feedback" id="pattern-feedback"></div>
            </div>
        `;

        container.innerHTML = html;

        // Setup tile click handlers
        this.setupPatternTileHandlers();
    }

    showPatternObserverPhase(rules, gameMode) {
        const container = document.getElementById('mini-game-container');
        if (!container) return;

        let html = `
            <div class="pattern-tiles-game">
                <h2>🧩 Pattern Tiles - Recreation Phase</h2>
                <p class="phase-instruction">Watch TV for timer</p>

                <div class="observer-panel">
                    <h3>👀 Observing</h3>
                    <p>Watching players recreate the pattern...</p>
                    <p class="suspense-text">Who will remember it best? 🧠</p>
                </div>
            </div>
        `;

        container.innerHTML = html;
    }

    renderTileGrid(grid, isInteractive) {
        let html = '';
        for (let i = 0; i < 4; i++) {
            for (let j = 0; j < 4; j++) {
                const tileValue = grid[i][j];
                const tileClass = tileValue === 1 ? 'tile-blue' : 'tile-white';
                const interactiveClass = isInteractive ? 'interactive' : '';
                const dataAttrs = isInteractive ? `data-row="${i}" data-col="${j}"` : '';

                html += `<div class="tile ${tileClass} ${interactiveClass}" ${dataAttrs}></div>`;
            }
        }
        return html;
    }

    setupPatternTileHandlers() {
        // Tile click handlers
        const tiles = document.querySelectorAll('.tile.interactive');
        tiles.forEach(tile => {
            tile.addEventListener('click', () => {
                const row = parseInt(tile.getAttribute('data-row'));
                const col = parseInt(tile.getAttribute('data-col'));

                // Toggle tile value (0 <-> 1)
                this.playerGrid[row][col] = this.playerGrid[row][col] === 0 ? 1 : 0;

                // Update tile appearance
                if (this.playerGrid[row][col] === 1) {
                    tile.classList.remove('tile-white');
                    tile.classList.add('tile-blue');
                } else {
                    tile.classList.remove('tile-blue');
                    tile.classList.add('tile-white');
                }
            });
        });

        // Submit button handler
        const submitBtn = document.getElementById('submit-pattern-btn');
        if (submitBtn) {
            submitBtn.addEventListener('click', () => {
                this.submitPatternGrid();
            });
        }
    }

    submitPatternGrid() {
        console.log('[PATTERN-TILES] submitPatternGrid called');
        if (!this.playerGrid) {
            console.error('[PATTERN-TILES] No grid to submit');
            return;
        }

        console.log('[PATTERN-TILES] Submitting grid:', JSON.stringify(this.playerGrid));

        // Send grid to server
        this.ws.send({
            type: 'mini_game_action',
            action: {
                type: 'submit_grid',
                grid: this.playerGrid
            }
        });
        console.log('[PATTERN-TILES] Grid submission sent to server');

        // Show feedback
        const feedback = document.getElementById('pattern-feedback');
        if (feedback) {
            feedback.textContent = '✓ Pattern submitted!';
            feedback.className = 'submission-feedback success';
        }

        // Disable submit button and tiles
        const submitBtn = document.getElementById('submit-pattern-btn');
        if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.textContent = 'Submitted ✓';
        }

        const tiles = document.querySelectorAll('.tile.interactive');
        tiles.forEach(tile => {
            tile.classList.remove('interactive');
            tile.style.cursor = 'default';
        });

        console.log('[PATTERN-TILES] Submitted grid:', this.playerGrid);
    }

    // ========== PLAYING AT A DISADVANTAGE ==========

    showPlayingAtDisadvantageUI(setup) {
        const atRiskPlayers = setup.at_risk_players || [];
        const isAtRisk = atRiskPlayers.includes(this.playerId);
        const rules = setup.rules || {};
        const answerPositions = setup.answer_positions || [1, 2, 3, 4];

        const container = document.getElementById('mini-game-container');
        if (!container) return;

        let html = `
            <div class="playing-at-disadvantage-game">
                <h2>⚠️ Playing at a Disadvantage</h2>
                <p class="timer-display">Time remaining: <span id="mini-game-timer-display">30</span>s</p>

                <!-- Rules Box -->
                <div class="game-rules-box disadvantage-rules">
                    <h3>${rules.title || '⚠️ Playing at a Disadvantage'}</h3>

                    <div class="rules-section">
                        <h4>How It Works:</h4>
                        <ul class="rules-list">
                            ${(rules.main_rules || []).map(rule => `<li>${rule}</li>`).join('')}
                        </ul>
                    </div>

                    <div class="rules-section consequence-section">
                        <p class="consequence-warning">${rules.consequence || ''}</p>
                    </div>
                </div>
        `;

        if (isAtRisk) {
            // Position selection UI for at-risk players
            html += `
                <div class="position-selection-container">
                    <h3>Choose Your Disabled Answer Position</h3>
                    <p class="selection-prompt">Which answer position will you be unable to select?</p>

                    <div class="position-buttons">
                        ${answerPositions.map(pos => `
                            <button class="position-btn" data-position="${pos}">
                                <span class="position-number">${pos}</span>
                                <span class="position-label">Position ${pos}</span>
                            </button>
                        `).join('')}
                    </div>

                    <div class="selection-feedback" id="disadvantage-feedback"></div>
                </div>
            `;
        } else {
            // Observer screen for safe players
            html += `
                <div class="observer-panel">
                    <h3>👀 Observing</h3>
                    <p>Watching the at-risk players choose their disadvantage...</p>
                    <p class="suspense-text">What will they choose? 🤔</p>
                </div>
            `;
        }

        html += `</div>`;

        container.innerHTML = html;

        if (isAtRisk) {
            this.setupPositionSelectionHandlers();
        }
    }

    setupPositionSelectionHandlers() {
        const positionButtons = document.querySelectorAll('.position-btn');
        let selectedPosition = null;

        positionButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                // Remove previous selection
                positionButtons.forEach(b => b.classList.remove('selected'));

                // Mark as selected
                btn.classList.add('selected');
                selectedPosition = parseInt(btn.getAttribute('data-position'));

                // Submit the selection
                this.submitPositionSelection(selectedPosition);
            });
        });
    }

    submitPositionSelection(position) {
        if (!position || position < 1 || position > 4) {
            console.error('[DISADVANTAGE] Invalid position:', position);
            return;
        }

        // Send selection to server
        this.ws.send({
            type: 'mini_game_action',
            action: {
                type: 'select_position',
                position: position
            }
        });

        // Show feedback
        const feedback = document.getElementById('disadvantage-feedback');
        if (feedback) {
            feedback.textContent = `✓ Position ${position} selected - This will be disabled for the rest of the game!`;
            feedback.className = 'selection-feedback success';
        }

        // Disable all buttons
        const positionButtons = document.querySelectorAll('.position-btn');
        positionButtons.forEach(btn => {
            btn.disabled = true;
            if (!btn.classList.contains('selected')) {
                btn.style.opacity = '0.5';
            }
        });

        console.log(`[DISADVANTAGE] Submitted position: ${position}`);
    }
}

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
    module.exports = MiniGamesManager;
}
