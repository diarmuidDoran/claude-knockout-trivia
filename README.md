# Knockout Trivia

A real-time multiplayer trivia game where players compete to be the last one standing. Answer questions correctly to stay in the game, while wrong answers lead to elimination mini-games in this fast-paced, knockout-style competition.

## Table of Contents

- [Game Features](#game-features)
- [Game Rules & Flow](#game-rules--flow)
- [Mini-Games](#mini-games-6-available)
- [Haunting Race](#haunting-race-)
- [Architecture](#architecture)
- [Quick Start](#quick-start)
- [Testing & Debug Tools](#testing--debug-tools)
- [Configuration](#configuration)
- [API Documentation](#api-documentation)
- [Troubleshooting](#troubleshooting)
- [Development](#development)
- [Project Structure](#project-structure)

---

## Game Features

- **Real-time Multiplayer**: WebSocket-based gameplay for instant synchronization
- **Knockout Mechanics**: Players who answer incorrectly play elimination mini-games
- **6 Mini-Games**: Various elimination games with different mechanics
- **Haunting Race**: Special end-game mode when 2 living players remain - race to column 20 with role swapping
- **Ghost Player System**: Eliminated players continue playing but cannot win
- **1,000 Questions**: Extensive question database across 16 categories
- **Multiple Difficulty Levels**: Easy, Medium, Hard, and Expert questions
- **Randomized Answer Positions**: Correct answers randomly placed in positions 1-4
- **30-Second Timer**: Quick-paced rounds keep the game exciting (20s in Haunting Race)
- **Room System**: Create private rooms or join existing games
- **Live Scoring**: Real-time score updates and player status
- **Auto-Return to Home**: TV automatically cleans up after 30 seconds if no rematch

---

## Game Rules & Flow

### Game Flow Diagram

```
Room Creation → Player Joining → Game Start (VIP) → Question Phase (30s)
→ Answer Collection → Results Display (3s) → Mini-Game Selection
→ Mini-Game Execution (30-60s) → Eliminations → Ghost Players Update
→ Next Question → [Repeat] → Last Player Standing Wins!
```

### Player Roles

#### VIP Player
- First player to join the room
- Controls when the game starts
- Controls rematch after game ends
- Can play normally once game begins

#### At-Risk Players
- Answered the previous question incorrectly
- Must participate in the mini-game
- At risk of becoming ghost players

#### Safe Players
- Answered the previous question correctly
- May participate in some mini-games (depends on mini-game)
- **Cannot be eliminated** - safe players never become ghosts

#### Ghost Players
- Previously eliminated in a mini-game
- Continue playing and earning points
- **Cannot win the game** - only living players can win
- Displayed with special ghost indicator 👻

### Question Phase (30 seconds)

1. **Question Display**: Question appears on TV screen and all mobile devices
2. **Answer Selection**: Players choose from 4 multiple-choice options
3. **Random Positions**: Correct answer is randomly placed in positions 1-4
4. **Submit Answer**: Players tap their choice (can change until time runs out)
5. **Timer Countdown**: 30-second timer displayed on TV

### Results Phase (3 seconds)

1. **Correct Answer Revealed**: Shown on TV and mobile devices
2. **Player Results**: Each player sees if they were correct
3. **Points Awarded**: Correct answers earn points
4. **Leaderboard Update**: Live leaderboard updates on TV

### Mini-Game Phase (30-60 seconds)

1. **Selection**: Random mini-game selected from available pool
2. **Setup**: Players assigned roles (at-risk, safe, observer)
3. **Gameplay**: Mini-game-specific mechanics (see Mini-Games section)
4. **Resolution**: Winner/loser determined
5. **Elimination**: Losing player(s) become ghosts

### Win Condition

**The last living (non-ghost) player wins!**

If all players are eliminated (all ghosts), the player with the highest score wins.

---

## Mini-Games (6 Available)

### 1. Chalices ☠️

**Concept:** Poisoners (safe players) poison chalices, Testers (at-risk players) choose which to drink.

**Duration:** 30 seconds

**How It Works:**
1. Safe players become **Poisoners** and each secretly select ONE chalice to poison
2. At-risk players become **Testers** and each select ONE chalice to drink
3. A chalice is poisoned if ANY poisoner selected it
4. After 30 seconds (or all selections made), results revealed
5. Testers who drank poisoned chalices are eliminated

**Elimination Rules:**
- If **multiple at-risk players**: Testers who drink poison become ghosts
- If **no safe players exist** (everyone answered wrong): One random chalice is automatically poisoned

**Win Condition (for Testers):** Choose a chalice that no poisoner selected

**Special Cases:**
- If all testers choose the same poisoned chalice, all are eliminated
- If no chalices are poisoned, all testers survive

---

### 2. Worst Answer 🗳️

**Concept:** At-risk players submit terrible answers to opinion questions. Everyone votes. Most votes = eliminated!

**Duration:** 30 seconds submission + 30 seconds voting

**How It Works:**
1. **Submission Phase (30s)**: At-risk players type ridiculous answers to opinion question
2. **Voting Phase (30s)**: ALL players (including ghosts!) vote for the worst answer
3. Results revealed: Player with most votes is eliminated
4. Ghost players can vote but cannot be eliminated

**Elimination Rules:**
- Player with most votes becomes a ghost
- Ties broken randomly
- Only at-risk players can be eliminated (safe players immune)

**Example Questions:**
- "What's the worst gift to give someone?"
- "What's the most useless superpower?"
- "What's the worst place to propose?"

**Strategy:** Be hilariously bad (or strategically mediocre)

---

### 3. Quick Math ➗

**Concept:** Fast-paced mental arithmetic race. Answer as many simple math questions as possible.

**Duration:** 45 seconds

**How It Works:**
1. Competing players see math questions instantly (no delay)
2. Questions are simple: addition, subtraction, multiplication, division
3. All numbers are 2 digits or less (≤99)
4. Players type answers and submit
5. Next question appears immediately after correct answer
6. Score = total correct answers

**Question Examples:**
- 47 + 23 = ?
- 12 × 8 = ?
- 72 ÷ 9 = ?
- 85 - 37 = ?

**Elimination Rules:**
- **Multiple at-risk players**: Lowest scorer eliminated (ties broken randomly)
- **Single at-risk vs safe players**: At-risk must score highest or be eliminated
- **Complete tie** (all same score): No one eliminated
- Safe players cannot be eliminated regardless of score

**Strategy:** Speed AND accuracy matter!

---

### 4. Grab More Points 💰

**Concept:** Prisoner's dilemma - grab bonus points or play it safe?

**Duration:** 30 seconds

**How It Works:**
1. At-risk players see two buttons: **GRAB** (take points) or **PASS** (no points)
2. Players make their choice secretly
3. After 30 seconds, choices revealed simultaneously

**Elimination Rules:**
- If **anyone grabs**: Players who PASSED are eliminated
- If **everyone grabs**: Everyone gets 50 points, no eliminations
- If **everyone passes**: Everyone survives, no points awarded

**Strategy:** Trust your opponents at your own risk!

**Example Scenarios:**
- 3 at-risk players: 1 grabs, 2 pass → 2 passers eliminated, grabber survives
- 2 at-risk players: Both grab → Both survive, both get 50 points
- 2 at-risk players: Both pass → Both survive, no points

---

### 5. Pattern Tiles 🧩

**Concept:** Memory game - memorize and recreate a pattern of blue/white tiles.

**Duration:** 10 seconds memorization + 30 seconds recreation

**How It Works:**
1. **Memorization Phase (10s)**: 4×4 grid of blue/white tiles shown to all players
2. Pattern disappears
3. **Recreation Phase (30s)**: Players get blank grids (all white)
4. Click white tiles → turn blue, click blue tiles → turn white
5. Recreate the pattern from memory
6. Can submit early or wait for timer
7. Accuracy calculated as percentage of correct tiles

**Elimination Rules:**
- **Multiple at-risk players**: Lowest accuracy eliminated
- **Single at-risk vs all**: At-risk must score higher than everyone or be eliminated
- Ties broken randomly

**Accuracy Calculation:** (Correct tiles / 16 total tiles) × 100%

**Strategy:** Focus on patterns, not individual tiles!

---

### 6. Playing at a Disadvantage ⚠️

**Concept:** Vote to disable one answer position (1, 2, 3, or 4) for the rest of the game. **NO ELIMINATIONS!**

**Duration:** 30 seconds

**How It Works:**
1. At-risk players vote on which answer position (1, 2, 3, or 4) to disable
2. Position with most votes is permanently disabled for those players
3. For all future questions, disabled position appears as 🚫 and cannot be selected
4. No one is eliminated - this is a **penalty game**

**Penalty:**
- Players have only 3 answer choices instead of 4
- If the correct answer appears in disabled position, impossible to answer correctly

**Voting:**
- Ties broken randomly
- All at-risk players get the same disabled position

**Strategy:** Hope the least likely position is chosen!

---

## Haunting Race 🏁

**Special End-Game Feature:** When only 2 living players remain, the Haunting Race begins!

### Concept

A high-stakes memory race where one player is the **Unicorn** 🦄 trying to reach the finish line, while **Ghosts** 👻 (eliminated players) try to catch and swap roles with the unicorn.

### How It Works

1. **Activation**: Automatically triggers when exactly 2 living (non-ghost) players remain
2. **Race Track**: 20-column race track displayed on TV and mobile
3. **Starting Positions**: All players start at column 1
4. **Role Assignment**:
   - One living player randomly becomes the **Unicorn** 🦄
   - Other living player becomes a **Ghost** 👻
   - All previously eliminated players join as **Ghosts** 👻

### Question Mechanics

**Duration:** 20 seconds per question

**Question Type:** True/False statement selection

**How Questions Work:**
1. Players see a topic with 2-3 statements
2. **Unicorn sees:** 2 statements (no ghost-only statements)
3. **Ghosts see:** 3 statements (including 1 ghost-only statement)
4. Players select which statements are TRUE
5. Submit when ready (or wait for 20-second timer)

**Movement Points:**
- +1 space for each TRUE statement correctly selected
- +1 space for each FALSE statement correctly NOT selected
- Maximum 3 spaces per question (for ghosts with 3 statements)
- Maximum 2 spaces per question (for unicorn with 2 statements)

### Movement Order

**CRITICAL RULE:** Unicorn ALWAYS moves first!

1. 🦄 **Unicorn moves** (based on correct answers)
2. ⏱️ **2-second delay** (visual pause so players see unicorn moved first)
3. 👻👻👻 **ALL ghosts move simultaneously** (based on correct answers)

**Why this matters:** If the unicorn reaches column 20, they win immediately - ghosts don't get to move that turn.

### Role Swap Mechanic

**When a Ghost catches the Unicorn:**

1. If any ghost lands on the SAME column as the unicorn (or passes them):
2. The fastest ghost (or random if tied) **becomes the new Unicorn** 🦄
3. The old unicorn **becomes a Ghost** 👻 and is pushed back 1 space
4. **Visual updates:**
   - Player icons swap (👻 → 🦄 and 🦄 → 👻)
   - Mobile screens update role messages
   - Question options update (2 vs 3 statements)

### Win Conditions

**Unicorn Wins:**
- Unicorn reaches column 20 first
- That player wins the entire game!
- Becomes 1st place regardless of trivia score

**If Ghosts Prevent Win:**
- Regular game continues after Haunting Race
- Normal win condition applies (last living player)

### Strategy

**For Unicorn:**
- Answer accurately to move faster
- Stay ahead of ghosts
- Reach column 20 to win immediately!

**For Ghosts:**
- Answer accurately to catch up
- Land on same column as unicorn to swap roles
- Become unicorn and race to victory!

### Visual Features

- **Race Track:** 20-column grid displayed on TV
- **Player Tokens:** Animated icons showing current positions
- **Role Indicators:** Clear labels for unicorn vs ghosts
- **Movement Animation:** Sequential movement (unicorn first, then ghosts)
- **Swap Animation:** Visual notification when roles swap
- **Instructions:** On-screen guidance for how to play

### Session Restoration

Players can refresh during Haunting Race and rejoin seamlessly:
- Reconnects to same race
- Restores current position
- Shows current question if active
- Maintains correct role (unicorn or ghost)

---

## Architecture

### Tech Stack

**Backend:**
- FastAPI (Python) - High-performance async API
- PostgreSQL - Question and game state database
- WebSockets - Real-time game communication
- SQLAlchemy - ORM for database operations

**Frontend:**
- HTML5/CSS3/JavaScript (Vanilla)
- WebSocket client for real-time updates
- Responsive design for mobile and TV displays

**Infrastructure:**
- Docker & Docker Compose
- Nginx for frontend serving

### WebSocket Communication Flow

```
1. Room Creation:
   TV → POST /api/rooms/create → Response: {room_code, player_id}
   TV → WS Connect: ws://host/ws/{room_code}/{player_id}

2. Player Joining:
   Mobile → POST /api/rooms/join → Response: {player_id, room_code}
   Mobile → WS Connect: ws://host/ws/{room_code}/{player_id}
   Backend → Broadcast: "player_joined" event to room

3. Game Start:
   VIP → POST /api/game/start
   Backend → Broadcast: "game_started" event

4. Question Phase:
   Backend → Broadcast: "new_question" event
   Players → POST /api/game/{room}/submit-answer
   Backend → Broadcast: "player_answered" event (real-time)
   Backend → Broadcast: "question_results" event

5. Mini-Game Phase:
   Backend → Broadcast: "mini_game_start" event
   Players → WS Send: "mini_game_action" with action data
   Backend → Broadcast: "mini_game_player_action" (live updates)
   Backend → Broadcast: "mini_game_results" event

6. Game End:
   Backend → Broadcast: "game_ended" event with final leaderboard
```

### WebSocket Events Reference

**Received by Clients:**
- `player_joined` - New player joined room
- `player_left` - Player left room
- `game_started` - Game has begun
- `new_question` - New question available (includes start_time for sync)
- `player_answered` - Another player answered (real-time feedback)
- `question_results` - Question results and correct answer
- `mini_game_start` - Mini-game beginning (includes game_name, setup data)
- `mini_game_phase_change` - Mini-game phase transition (e.g., voting phase)
- `mini_game_player_action` - Player action in mini-game (live updates)
- `mini_game_results` - Mini-game results and eliminations
- `game_ended` - Game over with final leaderboard

**Sent by Clients:**
- `player_answered` - Notify others of answer (after submission)
- `mini_game_action` - Mini-game action (choice, vote, answer, etc.)

### Frontend Architecture

**TV Display (tv.html):**
- Shows questions on large screen
- Displays live leaderboard
- Shows mini-game interface for all players
- Controlled by tv-app.js

**Mobile Player (mobile.html):**
- Personal answer selection
- Individual score tracking
- Mini-game participation interface
- Controlled by mobile-game.js

**Shared Components:**
- websocket.js - WebSocket connection manager
- mini-games.js - Mini-game UI renderer
- config.js - Application configuration

### Backend Architecture

```
app/
├── main.py              # FastAPI app, CORS, WebSocket endpoint
├── models/
│   ├── database.py      # Database connection & session
│   └── models.py        # SQLAlchemy models (Room, Player, Question, etc.)
├── routes/
│   ├── rooms.py         # Room creation/joining
│   └── game.py          # Game control, answers, leaderboard
├── services/
│   ├── game_service.py  # Core game logic & WebSocket broadcasting
│   └── mini_game_manager.py  # Mini-game lifecycle management
└── websockets/
    └── manager.py       # WebSocket connection management

mini_games/
├── base_mini_game.py    # Abstract base class for all mini-games
├── chalices.py          # Chalices implementation
├── worst_answer.py      # Worst Answer implementation
├── quick_math.py        # Quick Math implementation
├── grab_more_points.py  # Grab More Points implementation
├── pattern_tiles.py     # Pattern Tiles implementation
└── playing_at_disadvantage.py  # Playing at Disadvantage implementation
```

---

## Live Demo

**🎮 Play Now:** https://claude-knockout-trivia-production.up.railway.app/

- **TV Display:** https://claude-knockout-trivia-production.up.railway.app/tv.html
- **Mobile Players:** https://claude-knockout-trivia-production.up.railway.app/mobile.html

---

## Quick Start

### Using Docker (Recommended)

1. **Prerequisites:**
   - Docker and Docker Compose installed

2. **Start:**
   ```bash
   docker-compose up -d
   ```

3. **Initialize Database:**
   ```bash
   docker exec knockout-trivia-api python init_db.py
   docker exec knockout-trivia-api python seed_questions.py
   ```

4. **Access the Game:**
   - Mobile Players: http://localhost:3000/mobile.html
   - TV Display: http://localhost:3000/tv.html
   - API Docs: http://localhost:8000/docs

### Manual Setup (Development)

```bash
# Backend
cd backend
pip install -r requirements.txt
python init_db.py
python seed_questions.py
python -m uvicorn app.main:app --reload --port 8001

# Frontend (separate terminal)
cd frontend
python3 -m http.server 3000
```

**Access:**
- TV Display: http://localhost:3000/tv.html
- Mobile Players: http://localhost:3000/mobile.html
- API Docs: http://localhost:8001/docs

### Multi-Device Setup (LAN Play)

To allow players on different devices (phones, tablets) to connect:

```bash
# Start backend listening on all network interfaces
python -m uvicorn app.main:app --reload --port 8001 --host 0.0.0.0

# Find your computer's IP address
# Mac/Linux: ifconfig | grep inet
# Windows: ipconfig

# Players access: http://{YOUR_IP}:3000/mobile.html
# TV display: http://{YOUR_IP}:3000/tv.html
```

### How to Play

1. **Create Room:**
   - Open TV display (tv.html)
   - Click "Create Room"
   - Room code displayed on TV (e.g., "ABCDEF")

2. **Join Room:**
   - Players open mobile.html on their phones
   - Enter room code (auto-uppercase)
   - Enter player name (auto-uppercase, max 15 chars)
   - Click "Join Game"

3. **Start Game:**
   - VIP player clicks "Start Game" button
   - Game begins immediately

4. **Answer Questions:**
   - Read question on TV screen (or mobile)
   - Tap answer choice on mobile device
   - Answer positions are randomized (correct answer can be 1, 2, 3, or 4)
   - Can change answer until timer expires
   - Results show after 30 seconds

5. **Play Mini-Games:**
   - At-risk players (answered incorrectly) participate
   - Follow on-screen instructions
   - Complete within time limit
   - Lowest performer becomes a ghost

6. **Continue Playing:**
   - Ghost players keep answering questions for points
   - Last living player wins!
   - VIP can click "Rematch" to play again with same players

---

## Testing & Debug Tools

The project includes 7 specialized test files for development and QA. All test files are located in `/frontend/` and accessed via `http://localhost:3000/[filename].html`.

### Basic Connectivity Tests

#### test.html
**Purpose:** Verify frontend is accessible and serving correctly

**When to use:**
- Initial setup verification
- Confirming frontend server is running
- Quick sanity check

**What it tests:**
- Static file serving
- Basic HTML rendering
- Browser compatibility

**Access:** http://localhost:3000/test.html

**Expected result:** Page displays "Frontend is working" message

---

#### simple.html
**Purpose:** Test room joining API without full game UI

**When to use:**
- Backend API testing
- Room management debugging
- Join flow troubleshooting

**Features:**
- Simple form: Room Code + Player Name
- Join Game button
- Direct API call to `/api/rooms/join`
- Pre-filled test room code: MYXARQ

**Access:** http://localhost:3000/simple.html

**Expected behavior:**
- Successful join returns player ID
- Invalid room code shows error
- Can verify backend /api/rooms/join endpoint

---

### UI Component Tests

#### debug.html
**Purpose:** Test home screen UI components with debug information panel

**When to use:**
- Home screen button debugging
- Event listener verification
- UI state inspection

**Features:**
- Debug info panel showing:
  - Button state
  - Event listeners attached
  - Click event tracking
- Tests "Create Room" and "Join Game" buttons
- Real-time debug output

**Access:** http://localhost:3000/debug.html

**Expected behavior:**
- Shows debug panel with component states
- Logs button clicks
- Verifies event handlers attached correctly

---

#### test-simple.html
**Purpose:** Test join screen with loading state transitions

**When to use:**
- Screen transition debugging
- Loading state verification
- Join flow testing

**Features:**
- Join form with loading simulation
- 2-second loading screen
- Debug counter display
- Auto-increment counter to verify JS execution

**Access:** http://localhost:3000/test-simple.html

**Expected behavior:**
- Form submission triggers loading screen
- Loading shown for 2 seconds
- Transitions to waiting screen
- Counter increments every second

---

#### test-mobile.html
**Purpose:** Test mobile player join functionality

**When to use:**
- Mobile-specific join flow testing
- API endpoint verification
- Room code validation testing

**Features:**
- Mobile join form
- Auto-uppercase room code input
- API endpoint detection
- Error handling display

**Access:** http://localhost:3000/test-mobile.html

**Expected behavior:**
- Room code converts to uppercase automatically
- Join button triggers API call
- Shows success/error messages
- Validates room code format (6 letters)

---

### Game Logic Tests

#### test-shuffle.html
**Purpose:** Verify answer position randomization algorithm

**When to use:**
- Testing question answer shuffling
- Verifying even distribution
- Confirming no bias toward positions

**Features:**
- Shows 10 shuffle iterations visually
- Runs 100-iteration distribution analysis
- Displays position frequency chart
- Expected: ~25% per position (1, 2, 3, 4)

**How it works:**
- Simulates question with correct answer + 3 wrong answers
- Shuffles 100 times
- Tracks which position correct answer lands in
- Displays percentage distribution

**Access:** http://localhost:3000/test-shuffle.html

**Expected result:**
```
Position 1: ~25%
Position 2: ~25%
Position 3: ~25%
Position 4: ~25%
```

**Interpretation:** Deviation >5% from 25% indicates potential bias in randomization algorithm

---

### Comprehensive Mini-Game Testing

#### mini-games-test.html ⭐ (Most Important Test Tool)
**Purpose:** Comprehensive testing harness for all 6 mini-games in isolation

**When to use:**
- Mini-game development
- QA testing mini-game mechanics
- Isolated mini-game debugging
- Verifying elimination logic
- Testing edge cases

**Features:**
- **Configurable Player Setup:**
  - Set number of at-risk players (1-5)
  - Set number of safe players (0-5)
  - Set number of ghost players (0-3)
  - Auto-generates mock player IDs

- **All 6 Mini-Games Testable:**
  - Quick Math - Test racing, scoring, timeout
  - Pattern Tiles - Test memorization, recreation, accuracy
  - Chalices - Test poisoner/tester roles, elimination logic
  - Worst Answer - Test submission, voting phases
  - Grab More Points - Test prisoner's dilemma logic
  - Playing at Disadvantage - Test position voting, penalty application

- **Mock WebSocket Communication:**
  - Simulates WebSocket events
  - No backend required for basic testing
  - Can test timeout scenarios
  - Event logging to console

- **Interactive Player Controls:**
  - Simulate actions for each player
  - Test different choice combinations
  - Verify elimination logic
  - Test tie scenarios

- **Real-Time Event Logging:**
  - All mini-game actions logged
  - Phase transitions tracked
  - Elimination decisions visible
  - Detailed console output

**Access:** http://localhost:3000/mini-games-test.html

**Testing Workflow:**
1. Select mini-game to test
2. Configure player counts (at-risk, safe, ghost)
3. Click "Start Mini-Game"
4. Interact with mini-game UI
5. Observe results and check console logs

**Example Test Scenarios:**

*Quick Math - Tie Scenario:*
- At-risk: 2, Safe: 0
- Both players answer 0 questions correctly
- Expected: No elimination (complete tie)

*Chalices - All Poisoned:*
- At-risk: 3, Safe: 2
- Both safe players poison same chalice
- All 3 testers choose that chalice
- Expected: All 3 testers eliminated

*Pattern Tiles - Perfect Recreation:*
- At-risk: 1, Safe: 0
- Player recreates pattern 100% accurately
- Expected: Player survives (16/16 tiles = 100%)

---

### Testing Best Practices

1. **Start with basic tests** (test.html, simple.html) to verify setup
2. **Use mini-games-test.html** extensively during mini-game development
3. **Test edge cases:**
   - All players tie
   - Single player games
   - Timeout scenarios
   - All players eliminated simultaneously
4. **Monitor both browser console AND backend terminal** for debug logs
5. **Hard refresh** (Cmd+Shift+R or Ctrl+Shift+R) after code changes to clear cache

---

## Configuration

### Backend Configuration

#### Database Settings

**Development (SQLite - Default):**
```python
# No configuration needed
# Creates knockout_trivia.db in backend directory
```

**Production (PostgreSQL):**
```bash
# Set environment variable
export DATABASE_URL="postgresql://user:password@host:port/knockout_trivia"

# Or create .env file in backend directory
DATABASE_URL=postgresql://user:password@localhost:5432/knockout_trivia
```

#### Port Configuration

**Default port:** 8000 or 8001

**Change port:**
```bash
python -m uvicorn app.main:app --reload --port 8001
```

**Listen on all network interfaces** (for LAN play):
```bash
python -m uvicorn app.main:app --reload --port 8001 --host 0.0.0.0
```

#### CORS Configuration

Edit `backend/app/main.py`:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://your-domain.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Frontend Configuration

**Location:** `frontend/js/config.js`

**Key Settings:**

```javascript
// Backend connection
const API_BASE = 'http://localhost:8001';
const WS_BASE = 'ws://localhost:8001';

// Game timing
QUESTION_TIME_LIMIT: 30,  // seconds per question
MAX_PLAYERS_PER_ROOM: 10,

// UI timing
NOTIFICATION_DURATION: 3000,  // milliseconds
TIMER_WARNING_THRESHOLD: 10,  // seconds (yellow)
TIMER_DANGER_THRESHOLD: 5,    // seconds (red)
```

**Docker Mode Detection:**
- Port 80 or no port: Uses relative URLs (nginx proxy)
- Port 3000: Development mode, connects to backend on port 8001

**Multi-Device Setup:**
When accessing from mobile devices on your network, config.js automatically detects the hostname and connects to the backend using that IP address.

---

## API Documentation

### REST API Endpoints

#### Room Management

**POST /api/rooms/create**
```json
Request: {}
Response: {
  "room_code": "ABCDEF",
  "player_id": 1,
  "player_name": "VIP",
  "is_vip": true
}
```

**POST /api/rooms/join**
```json
Request: {
  "room_code": "ABCDEF",
  "player_name": "PLAYER1"
}
Response: {
  "room_code": "ABCDEF",
  "player_id": 2,
  "player_name": "PLAYER1",
  "is_vip": false
}
```

**GET /api/rooms/{room_code}**
```json
Response: {
  "code": "ABCDEF",
  "status": "active",
  "player_count": 3
}
```

**GET /api/rooms/{room_code}/players**
```json
Response: [
  {
    "id": 1,
    "name": "VIP",
    "is_vip": true,
    "is_ghost": false,
    "total_score": 150
  },
  ...
]
```

#### Game Control

**POST /api/game/start**
```json
Request: {
  "room_code": "ABCDEF",
  "player_id": 1,
  "total_questions": 10
}
Response: {
  "status": "started",
  "total_questions": 10
}
```

**POST /api/game/{room_code}/submit-answer**
```json
Request: {
  "player_id": 2,
  "question_id": 42,
  "selected_option_id": 168,
  "response_time": 12.5
}
Response: {
  "correct": true,
  "points_earned": 100,
  "total_score": 250
}
```

**POST /api/game/rematch**
```json
Request: {
  "room_code": "ABCDEF",
  "player_id": 1,
  "total_questions": 10
}
Response: {
  "status": "started"
}
```

### Interactive API Documentation

FastAPI provides automatic interactive API documentation:

- **Swagger UI:** http://localhost:8001/docs
- **ReDoc:** http://localhost:8001/redoc

Use these to explore endpoints, test requests, and see response schemas.

### WebSocket Endpoint

**Connection:** `ws://localhost:8001/ws/{room_code}/{player_id}`

**Message Format:**
```json
{
  "type": "event_type",
  "data": { ... }
}
```

See [WebSocket Events Reference](#websocket-events-reference) for all event types.

---

## Troubleshooting

### Connection Issues

**Problem:** Can't access frontend at localhost:3000

**Solutions:**
1. Verify frontend server is running:
   ```bash
   cd frontend
   python3 -m http.server 3000
   ```
2. Check terminal for error messages
3. Try accessing http://127.0.0.1:3000/tv.html directly
4. Verify port 3000 isn't in use by another application

---

**Problem:** Frontend can't connect to backend

**Solutions:**
1. Verify backend is running:
   ```bash
   curl http://localhost:8001/docs
   ```
2. Check `config.js` has correct backend port (8001 or 8000)
3. Hard refresh browser (Cmd+Shift+R or Ctrl+Shift+R) to clear cached config
4. Check browser console for connection errors
5. Verify CORS settings in `backend/app/main.py`

---

**Problem:** WebSocket connection fails

**Solutions:**
1. Check browser console for WebSocket errors
2. Verify room code is correct (6 uppercase letters)
3. Confirm backend is running and accessible
4. Check WebSocket URL in config.js: `ws://localhost:8001`
5. Try refreshing the page

---

**Problem:** Mobile device can't connect from different device

**Solutions:**
1. Restart backend with `--host 0.0.0.0`:
   ```bash
   python -m uvicorn app.main:app --reload --port 8001 --host 0.0.0.0
   ```
2. Find your computer's IP address (not 127.0.0.1)
3. Access: `http://{YOUR_IP}:3000/mobile.html`
4. Ensure firewall allows connections on ports 3000 and 8001
5. Verify both devices on same network

---

### Game Issues

**Problem:** Questions not loading

**Solutions:**
1. Verify database is initialized:
   ```bash
   cd backend
   python init_db.py
   python seed_questions.py
   ```
2. Check backend logs for database errors
3. Verify database file exists: `backend/knockout_trivia.db` (SQLite)
4. For PostgreSQL, verify DATABASE_URL is correct

---

**Problem:** Mini-game not appearing after incorrect answer

**Solutions:**
1. Check backend logs for mini-game selection messages:
   ```
   [DEBUG] Room XXX: Starting mini-game with N at-risk players
   [MINI-GAME] Room XXX: Selected game: [Game Name]
   ```
2. Verify at-risk players exist (at least 1 incorrect answer)
3. Check browser console for WebSocket events
4. Use `mini-games-test.html` to test mini-game in isolation

---

**Problem:** Mini-game ending too early or too late

**Solutions:**
1. Check backend logs for timeout messages:
   ```
   [MINI-GAME] Room XXX: Starting timeout timer for 45 seconds
   [MINI-GAME TIMEOUT] Room XXX: 45 seconds elapsed
   ```
2. Verify no old timeout tasks from previous games (should see "Canceling previous timeout task")
3. Check mini-game's `get_timeout_seconds()` method
4. For Pattern Tiles, verify frontend timeout cleared properly

---

**Problem:** Answer positions not randomized

**Solutions:**
1. Use `test-shuffle.html` to verify randomization
2. Check distribution - should be ~25% per position
3. View browser console for shuffle iterations
4. Verify question has correct + 3 wrong answers in database

---

**Problem:** Players eliminated incorrectly in mini-games

**Solutions:**
1. Enable debug logging (already enabled for Quick Math and Chalices)
2. Check backend terminal for detailed mini-game logs:
   ```
   [QUICK-MATH DEBUG] Scores: {player_id: score}
   [CHALICES DEBUG] Tester choices: {tester_id: chalice}
   ```
3. Verify game mode (at_risk_vs_at_risk or at_risk_vs_safe)
4. Check safe players cannot be eliminated
5. Verify tie handling (all tied = no elimination)

---

**Problem:** Chalices: Safe chalice eliminating tester

**Check debug logs:**
```
[CHALICES DEBUG] Poisoner X locked in chalice Y
[CHALICES DEBUG] Tester A chose chalice B
[CHALICES DEBUG] Poisoned chalices set: {Y}
[CHALICES DEBUG] Tester A: chose chalice B, poisoned chalices: {Y}, is_poisoned: False/True
```

Verify chalice numbers match correctly (0-indexed vs 1-indexed display issue).

---

### Database Issues

**Problem:** Database errors or corruption

**Solutions:**
```bash
# Reset database (WARNING: Deletes all data including rooms and players)
cd backend
python init_db.py
python seed_questions.py

# Verify database integrity
python verify_database.py

# Remove duplicate questions
python remove_duplicates.py
```

---

**Problem:** Questions repeating in same game

**Solutions:**
1. Check backend logs for used questions tracking
2. Verify `seed_questions.py` creates unique questions
3. Check database for duplicate questions:
   ```bash
   python verify_database.py
   python remove_duplicates.py
   ```

---

### Debug Mode & Logging

#### Backend Debug Logs

**Location:** Terminal where uvicorn is running

**Enable logging:** Already enabled for Quick Math and Chalices mini-games

**Log prefixes:**
- `[DEBUG]` - General game flow
- `[MINI-GAME]` - Mini-game lifecycle
- `[QUICK-MATH DEBUG]` - Quick Math detailed logging
- `[CHALICES DEBUG]` - Chalices detailed logging
- `[MINI-GAME TIMEOUT]` - Timeout task tracking
- `[ERROR]` - Error conditions

**Example workflow:**
1. Start backend: `python -m uvicorn app.main:app --reload --port 8001`
2. Watch terminal for log messages
3. Logs appear in real-time as game progresses
4. Copy relevant logs for bug reports

---

#### Frontend Debug Logs

**Location:** Browser Developer Tools Console (F12 or Cmd+Option+I)

**Enable:** Console open automatically captures logs

**Log prefixes:**
- `[MOBILE-GAME]` - Mobile game logic
- `[PATTERN-TILES]` - Pattern Tiles frontend
- `[QUICK-MATH]` - Quick Math frontend
- `[WebSocket]` - WebSocket connection events

**Viewing logs:**
1. Open browser DevTools (F12)
2. Click "Console" tab
3. Play game normally
4. Logs appear in real-time

**Hard refresh to clear cache:**
- Mac: Cmd + Shift + R
- Windows/Linux: Ctrl + Shift + R

---

### Performance Issues

**Problem:** Game laggy or slow

**Solutions:**
1. Check number of connected players (recommended: 2-8)
2. Reduce number of questions per game
3. Check network latency (especially on WiFi)
4. Close unnecessary browser tabs
5. Use modern browser (Chrome, Firefox, Safari)

---

**Problem:** WebSocket disconnects frequently

**Solutions:**
1. Check network stability
2. Verify backend isn't restarting (disable `--reload` for testing)
3. Check for WebSocket timeout settings
4. Monitor backend logs for connection errors

---

## Development

### Adding Questions

1. Edit the appropriate file in `backend/questions_data/`:
   - `easy_questions.py`
   - `medium_questions.py`
   - `hard_questions.py`
   - `expert_questions.py`

2. Format:
   ```python
   {
       "text": "What is the capital of France?",
       "category": "geography",
       "correct": "Paris",
       "wrong": ["London", "Berlin", "Madrid"]
   }
   ```

3. Seed:
   ```bash
   cd backend
   python seed_questions.py
   ```

**Categories:** coding, pop_culture, gaming, science, history, geography, sports, music, technology, entertainment, literature, general, art, dnd, fandom

### Adding a New Mini-Game

See [Mini-Games System Documentation](backend/mini_games/README.md) for detailed guide on creating new mini-games.

**Quick overview:**
1. Create new file in `backend/mini_games/`
2. Inherit from `BaseMiniGame`
3. Implement required methods: `setup()`, `process_player_action()`, `can_resolve()`, `resolve()`
4. Register in `backend/mini_games/__init__.py`
5. Add frontend UI in `frontend/js/mini-games.js`

### Project Documentation

- [Backend Documentation](backend/README.md) - Backend architecture and implementation
- [Mini-Games System](backend/mini_games/README.md) - Mini-game development guide
- [Question Management](backend/questions_data/README.md) - Question database structure
- [Developer Guidelines](CLAUDE.md) - Coding standards and architecture decisions

---

## Project Structure

```
claude-knockout-trivia/
├── backend/
│   ├── app/
│   │   ├── models/
│   │   │   ├── database.py      # Database connection & session
│   │   │   └── models.py        # SQLAlchemy models
│   │   ├── routes/
│   │   │   ├── rooms.py         # Room creation/joining endpoints
│   │   │   └── game.py          # Game control & answer submission
│   │   ├── services/
│   │   │   ├── game_service.py  # Core game logic & WebSocket
│   │   │   └── mini_game_manager.py  # Mini-game lifecycle
│   │   ├── websockets/
│   │   │   └── manager.py       # WebSocket connection management
│   │   └── main.py              # FastAPI app initialization
│   ├── mini_games/              # Mini-game implementations (6 total)
│   │   ├── __init__.py          # Mini-games registry
│   │   ├── base_mini_game.py    # Abstract base class
│   │   ├── chalices.py          # Chalices (30s)
│   │   ├── worst_answer.py      # Worst Answer (60s total)
│   │   ├── quick_math.py        # Quick Math (45s)
│   │   ├── grab_more_points.py  # Grab More Points (30s)
│   │   ├── pattern_tiles.py     # Pattern Tiles (40s total)
│   │   ├── playing_at_disadvantage.py  # Disadvantage (30s)
│   │   └── opinion_questions.py # Opinion questions data
│   ├── questions_data/          # Question database (1,000 questions)
│   │   ├── __init__.py
│   │   ├── easy_questions.py    # 85 easy questions
│   │   ├── medium_questions.py  # 169 medium questions
│   │   ├── hard_questions.py    # 257 hard questions
│   │   └── expert_questions.py  # 489 expert questions
│   ├── migrations/              # Database migration scripts
│   ├── init_db.py               # Database initialization
│   ├── seed_questions.py        # Question seeding
│   ├── verify_database.py       # Database verification utility
│   ├── remove_duplicates.py     # Cleanup utility
│   ├── requirements.txt         # Python dependencies
│   ├── Dockerfile               # Docker container config
│   └── README.md                # Backend documentation
├── frontend/
│   ├── tv.html                  # TV display interface ⭐
│   ├── mobile.html              # Mobile player interface ⭐
│   ├── js/
│   │   ├── config.js            # Configuration settings
│   │   ├── websocket.js         # WebSocket manager
│   │   ├── tv-app.js            # TV display logic
│   │   ├── mobile-game.js       # Mobile game logic
│   │   └── mini-games.js        # Mini-games UI manager
│   ├── css/
│   │   ├── styles.css           # Mobile styles
│   │   ├── game-styles.css      # Mobile game screen styles
│   │   ├── tv-styles.css        # TV display styles
│   │   └── mini-games.css       # Mini-game UI styles
│   ├── test.html                # Basic connectivity test
│   ├── debug.html               # UI debugging tool
│   ├── simple.html              # API testing form
│   ├── test-simple.html         # Join screen test
│   ├── test-shuffle.html        # Randomization verification
│   ├── test-mobile.html         # Mobile join test
│   ├── mini-games-test.html     # Comprehensive mini-game tester ⭐
│   └── nginx.conf               # Nginx configuration (Docker)
├── archive/                     # Deprecated SQL files
├── docker-compose.yml           # Docker multi-container config
├── CLAUDE.md                    # Developer guidelines & architecture
└── README.md                    # This file
```

**⭐ = Primary application files**

---

## Question Database

- **Total**: 1,000 unique questions
- **Categories**: 16 (Coding, Pop Culture, Gaming, Science, History, Geography, Sports, Music, Technology, Entertainment, Literature, General, Art, D&D, Fandom)
- **Difficulties**:
  - Easy: 85 questions
  - Medium: 169 questions
  - Hard: 257 questions
  - Expert: 489 questions

**Question Format:**
Each question has:
- Question text
- 1 correct answer
- 3 wrong answers
- Category
- Difficulty level

**Answer Randomization:**
For each question, the correct answer and 3 wrong answers are shuffled into random positions (1, 2, 3, 4). This ensures the correct answer is not always in the same position. Use `test-shuffle.html` to verify even distribution.

---

## Known Issues & Limitations

- **Browser Compatibility**: Modern browsers required (Chrome, Firefox, Safari, Edge)
- **Mobile Safari**: May require user interaction to establish WebSocket connection
- **Player Limit**: Recommended 2-8 players (10 max)
- **Network Latency**: High latency may cause synchronization issues
- **Database**: SQLite suitable for development only; use PostgreSQL for production

---

## Recent Updates

### 2025-12-04
- **✅ Railway Deployment Complete!**
  - Live at https://claude-knockout-trivia-production.up.railway.app/
  - Automatic database initialization and question seeding on startup
  - PostgreSQL database connected and operational
  - Frontend and backend fully integrated
  - WebSocket connections working across devices
  - Tested and verified on both desktop and mobile

### 2025-11-30
- **Added Haunting Race feature** - Special end-game mode when 2 living players remain
  - True/False statement-based race mechanics
  - Unicorn vs Ghosts role system with role swapping
  - 20-column race track with sequential movement animation
  - 2-second delay showing unicorn moves first, then all ghosts simultaneously
  - Session restoration support during Haunting Race
  - Winner automatically ranked 1st place regardless of trivia score
- **Pattern Tiles improvements:**
  - Shortened rules from 3 sections to 1 concise line
  - Reduced memorization/recreation time in instructions
- **Haunting Race bug fixes:**
  - Fixed session restoration AttributeError (question_topic → category)
  - Fixed timer display on TV screen (CSS selector specificity)
  - Fixed player role display updates after unicorn swap (getElementById → querySelector)
  - Fixed player token visual updates (immediate position refresh)
  - Added instructions for how to answer race questions
- **TV auto-return feature:**
  - TV automatically returns to home screen after 30 seconds if no rematch requested
  - Auto-cleanup deletes room and disconnects
  - Timer cancelled if rematch is started

### 2025-11-25
- Fixed mini-game timeout tasks not being canceled (causing early game endings)
- Fixed frontend config to connect to correct backend port (8001)
- Removed redundant files (index.html, uno-knockout-trivia.html, unused JS files)
- Added comprehensive debug logging for Chalices and Quick Math
- Fixed Pattern Tiles grid container spacing
- Added uppercase enforcement for player names
- Fixed next question auto-load after mini-games

### 2025-11-23
- 6 mini-games fully integrated
- Answer positions randomly shuffled for each question
- Fixed mini-game player detection and participation
- Removed strategy hints from Playing at a Disadvantage
- Quick Math questions limited to 2-digit numbers
- 30-second voting time for Worst Answer

---

## License

[Add license information]

## Credits

Built with FastAPI, PostgreSQL, and WebSockets.

---

**For detailed backend documentation:** [backend/README.md](backend/README.md)
**For mini-games development:** [backend/mini_games/README.md](backend/mini_games/README.md)
**For developer guidelines:** [CLAUDE.md](CLAUDE.md)
