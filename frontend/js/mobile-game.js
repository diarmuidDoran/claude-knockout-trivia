// Mobile Game Logic - Question handling, timer, answers
let currentQuestion = null;
let questionStartTime = null;
let timerInterval = null;
let playerScore = 0;
let hasAnswered = false;

// Handle new question from WebSocket
function handleNewQuestion(data) {
    console.log('New question received:', data);

    currentQuestion = data.question;
    hasAnswered = false;

    // Store question start time for scoring
    if (data.start_time) {
        questionStartTime = new Date(data.start_time).getTime();
    } else {
        questionStartTime = Date.now();
    }

    // Hide mini-game container if it's still visible
    const miniGameContainer = document.getElementById('mini-game-container');
    if (miniGameContainer) {
        console.log('[MOBILE-GAME] Hiding mini-game container for new question');
        miniGameContainer.style.display = 'none';
        miniGameContainer.innerHTML = '';
    }

    // Show game screen
    document.getElementById('waiting-screen').classList.add('hidden');
    document.getElementById('game-screen').classList.remove('hidden');

    // Display question immediately (no delay)
    document.getElementById('question-category').textContent = currentQuestion.category.toUpperCase();
    document.getElementById('question-text').textContent = currentQuestion.text;

    // Get disabled position for this player (from Playing at a Disadvantage mini-game)
    const disabledPositions = data.disabled_positions || {};
    const myDisabledPosition = disabledPositions[playerId];

    // Display answer options
    const answersContainer = document.getElementById('answers-container');
    answersContainer.innerHTML = '';

    // Sort options by their order property to ensure consistent display across all devices
    const sortedOptions = [...currentQuestion.options].sort((a, b) => a.order - b.order);

    sortedOptions.forEach((option, index) => {
        const button = document.createElement('button');
        button.className = 'answer-btn';
        button.textContent = option.text;
        button.dataset.optionId = option.id;

        // Check if this position is disabled for the current player
        if (myDisabledPosition && option.order === myDisabledPosition) {
            button.classList.add('disabled-position');
            button.disabled = true;
            button.title = 'This position is disabled (Playing at a Disadvantage)';
            // Add visual indicator
            button.textContent = `🚫 ${option.text}`;
        } else {
            button.addEventListener('click', () => submitAnswer(option.id));
        }

        answersContainer.appendChild(button);
    });

    // Show question container
    const questionContainer = document.getElementById('question-container');
    const resultContainer = document.getElementById('result-container');

    questionContainer.classList.remove('hidden');
    resultContainer.classList.add('hidden');
    document.getElementById('points-earned').parentElement.style.display = 'block';
    document.getElementById('total-score').parentElement.style.display = 'block';
}

// Timer removed - now only shown on TV screen
// Players see question immediately when it's broadcast

// Submit answer
async function submitAnswer(optionId) {
    if (hasAnswered) return;

    hasAnswered = true;
    const responseTime = (Date.now() - questionStartTime) / 1000; // seconds

    // Disable all answer buttons
    document.querySelectorAll('.answer-btn').forEach(btn => {
        btn.disabled = true;
        if (btn.dataset.optionId === String(optionId)) {
            btn.classList.add('selected');
        }
    });

    try {
        const response = await fetch(`${CONFIG.API_BASE_URL}/api/game/${currentRoom}/submit-answer`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                player_id: playerId,
                question_id: currentQuestion.id,
                selected_option_id: optionId,
                response_time: responseTime
            })
        });

        if (response.ok) {
            const result = await response.json();
            showResult(result);

            // Notify WebSocket that player answered
            if (wsManager) {
                wsManager.send({
                    type: 'player_answered',
                    player_id: playerId,
                    question_id: currentQuestion.id
                });
            }
        } else {
            const error = await response.json();
            showNotification(error.detail || 'Failed to submit answer', 'error');
        }
    } catch (error) {
        console.error('Error submitting answer:', error);
        showNotification('Network error', 'error');
    }
}

// Show result after answering
function showResult(result) {
    playerScore = result.total_score;

    // Update score display
    document.getElementById('player-score').textContent = playerScore;

    // Hide question, show result
    document.getElementById('question-container').classList.add('hidden');
    document.getElementById('result-container').classList.remove('hidden');

    // Show result details
    const resultIcon = document.getElementById('result-icon');
    const resultMessage = document.getElementById('result-message');

    if (result.correct) {
        resultIcon.textContent = '✅';
        resultIcon.style.color = '#4CAF50';
        resultMessage.textContent = 'Correct!';
        resultMessage.style.color = '#4CAF50';
    } else {
        resultIcon.textContent = '❌';
        resultIcon.style.color = '#f44336';
        resultMessage.textContent = 'Incorrect';
        resultMessage.style.color = '#f44336';
    }

    document.getElementById('points-earned').textContent = result.points_earned;
    document.getElementById('total-score').textContent = result.total_score;
}

// Show timeout message
function showTimeoutMessage() {
    document.getElementById('question-container').classList.add('hidden');
    document.getElementById('result-container').classList.remove('hidden');

    document.getElementById('result-icon').textContent = '⏱️';
    document.getElementById('result-message').textContent = 'Time\'s Up!';
    document.getElementById('points-earned').textContent = '0';
}

// Handle timer expired event (instant timeout notification from server)
function handleTimerExpired(data) {
    console.log('Timer expired:', data);

    // If player hasn't answered yet, show timeout message immediately
    if (!hasAnswered) {
        showTimeoutMessage();
    }
}

// Handle question results (for showing correct answer and leaderboard)
function handleQuestionResults(data) {
    console.log('Question results:', data);

    // If player hasn't answered yet, show timeout message
    if (!hasAnswered) {
        showTimeoutMessage();
    }

    // Update the result to show correct answer info
    const correctAnswer = data.correct_answer;
    if (correctAnswer) {
        const resultContainer = document.getElementById('result-container');
        if (!resultContainer.classList.contains('hidden')) {
            // If we're already showing results, add correct answer info
            const resultMessage = document.getElementById('result-message');
            if (resultMessage) {
                const currentText = resultMessage.textContent;
                resultMessage.innerHTML = currentText + `<br><small>Correct: ${correctAnswer.text}</small>`;
            }
        }
    }

    // Results will be shown for 5 seconds, then next question will arrive
}

// Handle game ended
function handleGameEnded(data) {
    console.log('Game ended:', data);

    // Clear timer
    if (timerInterval) clearInterval(timerInterval);

    // Hide haunting race screen if it's active
    const hauntingRaceScreen = document.getElementById('haunting-race-screen');
    if (hauntingRaceScreen) {
        hauntingRaceScreen.classList.add('hidden');
        hauntingRaceScreen.classList.remove('active');
    }

    // Clean up haunting race manager if it exists
    if (window.hauntingRaceManager) {
        window.hauntingRaceManager.cleanup();
    }

    // Hide game screen, show game over screen
    document.getElementById('game-screen').classList.add('hidden');
    document.getElementById('game-over-screen').classList.remove('hidden');

    // Show final results with error handling
    try {
        if (!data || !data.final_leaderboard) {
            console.error('[MOBILE-GAME-END] Error: Missing final_leaderboard data', data);
            document.getElementById('player-final-rank').textContent = '?';
            document.getElementById('player-final-score').textContent = '0';
            return;
        }

        if (data.final_leaderboard.length === 0) {
            console.warn('[MOBILE-GAME-END] Warning: Empty final_leaderboard');
            return;
        }

        console.log('[MOBILE-GAME-END] Final leaderboard:', data.final_leaderboard);

        // Find player's rank
        const playerRank = data.final_leaderboard.findIndex(p => p.player_id === playerId);
        const playerData = data.final_leaderboard[playerRank];

        if (playerData) {
            // Display player's rank
            const rankSuffix = (rank) => {
                if (rank === 1) return '1st';
                if (rank === 2) return '2nd';
                if (rank === 3) return '3rd';
                return `${rank}th`;
            };

            document.getElementById('player-final-rank').textContent = rankSuffix(playerRank + 1);
            document.getElementById('player-final-score').textContent = playerData.total_score;

            // Add special styling for top 3
            const rankCard = document.getElementById('player-rank-display');
            if (playerRank === 0) {
                rankCard.style.background = 'linear-gradient(135deg, #FFD700 0%, #FFA500 100%)';
                rankCard.style.color = 'white';
            } else if (playerRank === 1) {
                rankCard.style.background = 'linear-gradient(135deg, #C0C0C0 0%, #808080 100%)';
                rankCard.style.color = 'white';
            } else if (playerRank === 2) {
                rankCard.style.background = 'linear-gradient(135deg, #CD7F32 0%, #8B4513 100%)';
                rankCard.style.color = 'white';
            }
        } else {
            console.error('[MOBILE-GAME-END] Error: Player not found in leaderboard');
            document.getElementById('player-final-rank').textContent = '?';
            document.getElementById('player-final-score').textContent = '0';
        }

        // Display final leaderboard
        const leaderboardContainer = document.getElementById('mobile-final-leaderboard');
        leaderboardContainer.innerHTML = '';

        data.final_leaderboard.forEach((player, index) => {
            const rank = index + 1;
            const medal = rank === 1 ? '🥇' : rank === 2 ? '🥈' : rank === 3 ? '🥉' : `${rank}.`;
            const isCurrentPlayer = player.player_id === playerId;

            const item = document.createElement('div');
            item.className = `final-standing-item ${isCurrentPlayer ? 'current-player' : ''}`;
            item.innerHTML = `
                <div class="final-standing-rank">${medal}</div>
                <div class="final-standing-name">${player.player_name}${isCurrentPlayer ? ' (You)' : ''}</div>
                <div class="final-standing-score">${player.total_score} pts</div>
            `;

            leaderboardContainer.appendChild(item);
        });

        // Show VIP options or waiting message
        if (isVIP) {
            document.getElementById('vip-game-options').style.display = 'flex';
            document.getElementById('waiting-vip-message').style.display = 'none';
        } else {
            document.getElementById('vip-game-options').style.display = 'none';
            document.getElementById('waiting-vip-message').style.display = 'block';
        }
    } catch (error) {
        console.error('[MOBILE-GAME-END] Error displaying game results:', error);
        // Show error to user
        document.getElementById('player-final-rank').textContent = 'Error';
        document.getElementById('player-final-score').textContent = '0';
    }
}

function handleRematchStarted(data) {
    console.log('Rematch started:', data);

    // Clear timer if running
    if (timerInterval) clearInterval(timerInterval);

    // Hide haunting race screen if it's active
    const hauntingRaceScreen = document.getElementById('haunting-race-screen');
    if (hauntingRaceScreen) {
        hauntingRaceScreen.classList.add('hidden');
        hauntingRaceScreen.classList.remove('active');
    }

    // Clean up haunting race manager if it exists
    if (window.hauntingRaceManager) {
        window.hauntingRaceManager.cleanup();
    }

    // Hide mini-game container if it's visible
    const miniGameContainer = document.getElementById('mini-game-container');
    if (miniGameContainer) {
        miniGameContainer.style.display = 'none';
        miniGameContainer.innerHTML = '';
    }

    // Reset game state
    playerScore = 0;
    hasAnswered = false;
    currentQuestion = null;

    // Hide all game screens
    document.getElementById('game-screen').classList.add('hidden');
    document.getElementById('game-over-screen').classList.add('hidden');

    // Show waiting screen
    document.getElementById('waiting-screen').classList.remove('hidden');

    // Show rematch message
    showNotification('Rematch starting! All scores reset.', 'success');
}
