# Mini-Game System Implementation Summary

## Overview

The mini-game system has been implemented to add elimination games between trivia questions. Players who answer incorrectly participate in mini-games that determine who gets eliminated and becomes a "ghost player."

## Implementation Date

**2025-11-18**

## What Was Created

### 1. Core Architecture

**Base Mini-Game System** ([backend/mini_games/base_mini_game.py](backend/mini_games/base_mini_game.py)):
- `BaseMiniGame` - Abstract base class for all mini-games
- `MiniGameResult` - Data class for mini-game outcomes
- `MiniGamePhase` - Enum for game lifecycle phases
- Timeout handling
- Player action processing

**Mini-Game Manager** ([backend/app/services/mini_game_manager.py](backend/app/services/mini_game_manager.py)):
- Selects appropriate mini-game based on player count
- Manages mini-game lifecycle
- Processes player actions
- Resolves games and updates player statuses
- Handles timeouts

### 2. Mini-Games Implemented

#### First Mini-Game: Chalices

**File**: [backend/mini_games/chalices.py](backend/mini_games/chalices.py)

**Mechanics**:
- Players who answered correctly = "Poisoners"
- Players who answered incorrectly = "Testers"
- Number of chalices = max(total_players, 3)
- Poisoners vote on which chalices to poison
- Testers choose which chalice to drink
- Drink poison = eliminated (become ghost)

**Features**:
- 45-second timeout
- Majority voting for poisoning
- Random assignment on timeout
- Supports 1+ testers

#### Second Mini-Game: Worst Answer

**File**: [backend/mini_games/worst_answer.py](backend/mini_games/worst_answer.py)

**Mechanics**:
- Players who answered incorrectly submit worst answers to opinion questions
- All players (safe, at-risk, and ghosts) vote on the worst answer
- Player with most votes = eliminated (become ghost)
- Players cannot vote for their own answer

**Features**:
- Two-phase system: submission (30s) → voting (20s)
- Opinion questions from separate module
- Input sanitization (max 30 chars, alphanumeric + basic punctuation)
- Vote counting with random tie-breaking
- 50+ opinion questions available
- Supports 1+ at-risk players

#### Third Mini-Game: Quick Math

**File**: [backend/mini_games/quick_math.py](backend/mini_games/quick_math.py)

**Mechanics**:
- At-risk players compete in a mental math race
- 45-second race to answer as many questions as possible
- Two game modes: at-risk vs at-risk OR at-risk vs safe players
- Each correct answer = 1 point
- Lowest scorer (or at-risk player who doesn't place 1st) eliminated

**Features**:
- Request/response pattern for instant question delivery
- Simple arithmetic: addition, subtraction, multiplication, division
- Optimistic UI updates for fast feedback
- Real-time score tracking
- Question examples: "7 + 14", "8 × 6", "24 ÷ 4", "15 - 8"
- Two elimination modes based on player counts
- Supports 1+ at-risk players

#### Fourth Mini-Game: Grab More Points

**File**: [backend/mini_games/grab_more_points.py](backend/mini_games/grab_more_points.py)

**Mechanics**:
- Prisoner's dilemma game where at-risk players grab bonus points (0-1000)
- Points are ALWAYS added to player scores regardless of outcome
- If no one takes points: Everyone survives
- If some take points: Those who didn't take points become ghosts
- If all take points: Everyone becomes a ghost
- 30-second decision time

**Features**:
- Classic game theory prisoner's dilemma
- Dynamic button text: "No points thanks" vs "Give me the points!"
- Visual feedback for greedy vs noble choices
- Points awarded before eliminations applied
- Requires minimum 2 at-risk players
- Strategic gameplay with trust and greed mechanics
- Supports 2+ at-risk players

#### Fifth Mini-Game: Pattern Tiles

**File**: [backend/mini_games/pattern_tiles.py](backend/mini_games/pattern_tiles.py)

**Mechanics**:
- Memory-based game where players memorize and recreate a pattern of blue and white tiles
- 4x4 grid with randomly placed blue (1) and white (0) tiles
- Two-phase gameplay: memorization (10s) → recreation (30s)
- Pattern shown on TV screen for 10 seconds
- Players get blank (all white) grids to recreate the pattern
- Click white tile → turns blue; click blue tile → turns white
- Accuracy calculated as percentage of matching tiles
- Two game modes: at-risk vs at-risk OR at-risk vs all

**Features**:
- Random 4x4 pattern generation (roughly 50/50 blue/white)
- Visual grid display with black tile borders
- Two-phase timer system (10s + 30s = 40s total)
- Interactive tile toggling
- Early submission option
- Percentage accuracy calculation
- Observer screen for non-competing players
- Two elimination modes based on player counts
- Supports 1+ at-risk players

### 3. Database Changes

**Player Model Updates** ([backend/app/models/models.py](backend/app/models/models.py)):
```python
class Player(Base):
    # ... existing fields ...
    is_ghost = Column(Boolean, default=False)  # NEW
    eliminated_at = Column(DateTime, nullable=True)  # NEW
```

**Migration Script** ([backend/migrations/add_ghost_player_fields.py](backend/migrations/add_ghost_player_fields.py)):
```bash
python backend/migrations/add_ghost_player_fields.py
```

### 4. Opinion Questions Module

**File**: [backend/mini_games/opinion_questions.py](backend/mini_games/opinion_questions.py)

Created dedicated module for Worst Answer opinion questions:
- 50+ opinion questions across categories
- Categories: Entertainment & Pop Culture, Food & Drink, Social Situations, Daily Life
- Helper functions: `get_random_question()`, `get_all_questions()`, `add_custom_question()`
- Examples: "What is the worst song to sing for karaoke?", "What is the best food as a last meal?"

### 5. Documentation

Created comprehensive documentation:

1. **[Mini-Games README](backend/mini_games/README.md)**
   - System overview
   - How to create new mini-games
   - Chalices and Worst Answer game details
   - Testing guidelines

2. **[Integration Guide](backend/MINI_GAME_INTEGRATION.md)**
   - Step-by-step integration instructions
   - Code examples for each integration point
   - WebSocket message formats
   - Troubleshooting guide

3. **[Root README Updates](README.md)**
   - Added mini-game features
   - Updated "How to Play" section
   - Added ghost player explanation
   - Project structure updated

## Game Flow

```
┌─────────────────────────────────────────────┐
│  Question (30s timer)                       │
└────────────────┬────────────────────────────┘
                 ▼
┌─────────────────────────────────────────────┐
│  Show Results                               │
│  - Correct players highlighted              │
│  - Incorrect players highlighted            │
└────────────────┬────────────────────────────┘
                 ▼
┌─────────────────────────────────────────────┐
│  Mini-Game Start                            │
│  - Roles assigned (Poisoners/Testers)       │
│  - Rules explained                          │
│  - Timer starts (45s)                       │
└────────────────┬────────────────────────────┘
                 ▼
┌─────────────────────────────────────────────┐
│  Players Make Choices                       │
│  - Poisoners vote on chalices              │
│  - Testers choose chalice to drink         │
└────────────────┬────────────────────────────┘
                 ▼
┌─────────────────────────────────────────────┐
│  Mini-Game Resolution                       │
│  - Determine poisoned chalices              │
│  - Check tester choices                     │
│  - Eliminate players who drank poison       │
└────────────────┬────────────────────────────┘
                 ▼
┌─────────────────────────────────────────────┐
│  Update Player Statuses                     │
│  - Set is_ghost = True for eliminated       │
│  - Set eliminated_at timestamp              │
│  - Broadcast results                        │
└────────────────┬────────────────────────────┘
                 ▼
┌─────────────────────────────────────────────┐
│  Check Game Status                          │
│  - 0-1 living players → End Game           │
│  - 2+ living players → Next Question       │
└─────────────────────────────────────────────┘
```

## Files Created

### Backend Core

```
backend/
├── mini_games/
│   ├── __init__.py                    # Mini-game registry
│   ├── base_mini_game.py              # Base class (300 lines)
│   ├── chalices.py                    # Chalices game (250 lines)
│   ├── worst_answer.py                # Worst Answer game (290 lines)
│   ├── quick_math.py                  # Quick Math game (410 lines)
│   ├── grab_more_points.py            # Grab More Points game (230 lines)
│   ├── pattern_tiles.py               # Pattern Tiles game (402 lines)
│   ├── opinion_questions.py           # Opinion questions (130 lines)
│   └── README.md                      # Documentation
│
├── app/
│   ├── models/
│   │   └── models.py                  # Updated with ghost fields
│   └── services/
│       └── mini_game_manager.py       # Manager service (280 lines)
│
├── migrations/
│   └── add_ghost_player_fields.py     # Database migration
│
├── MINI_GAME_INTEGRATION.md           # Integration guide
└── README.md                          # Updated backend docs
```

### Project Root

```
claude-knockout-trivia/
├── README.md                          # Updated with mini-games
└── MINI_GAME_IMPLEMENTATION.md        # This file
```

## Ghost Player System

### What is a Ghost Player?

- **Eliminated but Still Playing**: Players who lost in a mini-game
- **Can Answer Questions**: Continue participating in trivia
- **Earn Points**: Score still tracked on leaderboard
- **Cannot Win**: Only living (non-ghost) players can win
- **Visual Indicator**: Displayed with special styling in UI

### Benefits

1. **No Player Elimination Frustration**: Players stay engaged
2. **Support Living Players**: Can still interact and have fun
3. **Learn and Compete**: Continue answering questions
4. **High Score Competition**: Compete for overall high score

## Integration Steps for Developers

### Step 1: Run Database Migration

```bash
cd backend
python migrations/add_ghost_player_fields.py
```

### Step 2: Add Mini-Game Manager to Game Service

```python
from app.services.mini_game_manager import MiniGameManager

class GameService:
    def __init__(self, connection_manager):
        self.mini_game_manager = MiniGameManager()
```

### Step 3: Integrate After Question Results

After showing question results, start a mini-game:

```python
# Determine correct/incorrect players
correct_players = [...]
incorrect_players = [...]

# Start mini-game
if incorrect_players:
    mini_game_data = self.mini_game_manager.start_mini_game(
        room_code, incorrect_players, correct_players, total_players
    )
    await self.broadcast(room_code, mini_game_data)
```

### Step 4: Handle Mini-Game Actions

Add WebSocket handler:

```python
elif message_type == "mini_game_action":
    await self.handle_mini_game_action(room_code, player_id, data)
```

### Step 5: Resolve and Continue

```python
# Resolve mini-game
result = self.mini_game_manager.resolve_mini_game(room_code, db)

# Broadcast results
await self.broadcast(room_code, {...})

# Continue to next question
await self.next_question(room_code)
```

**Complete integration guide**: [MINI_GAME_INTEGRATION.md](backend/MINI_GAME_INTEGRATION.md)

## WebSocket Message Types

### New Message Types

**TO Frontend**:
- `mini_game_start` - Game begins
- `mini_game_player_action` - Player acted
- `mini_game_results` - Game resolved
- `mini_game_timeout` - Time expired

**FROM Frontend**:
- `mini_game_action` - Player's choice/vote

**Complete message specifications**: See [Integration Guide](backend/MINI_GAME_INTEGRATION.md#websocket-messages)

## Frontend Requirements

### UI Components Needed

1. **Mini-Game Introduction Screen**
   - Game name and rules
   - Player roles
   - Timeout countdown

2. **Role-Specific UI**
   - Poisoner UI: Select chalices to poison
   - Tester UI: Select chalice to drink
   - Action confirmation

3. **Results Screen**
   - Show poisoned chalices
   - Player choices
   - Elimination animations
   - Ghost player indicators

4. **Ghost Player Indicators**
   - Special styling for eliminated players
   - Badge/icon showing ghost status
   - Different leaderboard display

### Example Frontend Flow

```javascript
// Handle mini-game start
websocket.on('mini_game_start', (data) => {
    showMiniGameIntro(data);
    const myRole = determineRole(data.setup);
    showRoleUI(myRole, data.setup);
    startTimer(data.timeout);
});

// Send action
function sendChoice(choice) {
    websocket.send({
        type: 'mini_game_action',
        action: choice
    });
}

// Handle results
websocket.on('mini_game_results', (data) => {
    showEliminationAnimation(data.eliminated);
    updateGhostPlayers(data.eliminated);
    displayResults(data.game_data);
});
```

## Testing

### Unit Tests

Test files to create:
- `tests/test_chalices.py`
- `tests/test_mini_game_manager.py`
- `tests/test_ghost_players.py`

### Integration Tests

- Full game flow with mini-games
- Timeout handling
- Edge cases (all correct, all incorrect, etc.)

### Manual Testing Checklist

- [ ] Question answered correctly/incorrectly
- [ ] Mini-game starts with correct roles
- [ ] Poisoners can vote
- [ ] Testers can choose chalice
- [ ] Timeout works correctly
- [ ] Players eliminated correctly
- [ ] Ghost status applied
- [ ] Game continues to next question
- [ ] End game with living players only
- [ ] Leaderboard shows ghosts correctly

## Future Enhancements

### Additional Mini-Games

Ideas for new mini-games:

1. **Lightning Round** - Quick question, fastest survives
2. **Rock Paper Scissors** - Tournament style elimination
3. **Hot Potato** - Pass token, explodes randomly
4. **Memory Match** - Match pairs, fewest eliminated
5. **Trivia Duel** - Head-to-head quick questions

### System Enhancements

- Mini-game difficulty scaling
- Player preferences (favorite games)
- Statistics tracking
- Replay system
- Custom mini-game creation UI

## Performance Considerations

- Mini-games add ~45-60 seconds per question
- Async operations prevent blocking
- Clean up mini-game data after resolution
- Consider player count for game selection
- WebSocket message optimization

## Known Limitations

1. **Six Mini-Games**: Chalices, Worst Answer, Quick Math, Grab More Points, Pattern Tiles, and Playing at a Disadvantage implemented, more games can be added
2. **No Game Customization**: Can't disable mini-games or choose specific games yet
3. **No Statistics**: Mini-game performance not tracked yet

## Next Steps

### Immediate (Required)

1. **Run Database Migration**: Execute `python3 backend/migrations/add_disabled_answer_position.py` to add the disabled position field
2. **Test Integration**: End-to-end testing of full flow with all six games
3. **Verify WebSocket Message Flow**: Ensure all games work correctly with WebSocket communication
4. **Test Edge Cases**: Single player, all timeout, tie scenarios, Pattern Tiles accuracy calculations
5. **Test Playing at a Disadvantage Integration**: Verify disabled positions display correctly in trivia UI

### Short Term

1. Implement 2-3 more mini-games (Lightning Round, Rock Paper Scissors, etc.)
2. Add mini-game statistics tracking
3. Create admin panel for game selection
4. Add player preferences

### Long Term

1. Custom mini-game builder
2. Community-created mini-games
3. Mini-game tournaments
4. Achievement system

## Documentation Links

- **[Mini-Games README](backend/mini_games/README.md)** - Complete mini-game system docs
- **[Integration Guide](backend/MINI_GAME_INTEGRATION.md)** - Step-by-step integration
- **[Root README](README.md)** - Project overview with mini-games
- **[Backend README](backend/README.md)** - Backend documentation

## Support & Troubleshooting

See [Integration Guide - Troubleshooting](backend/MINI_GAME_INTEGRATION.md#troubleshooting) for:
- Common issues
- Debug steps
- Error messages
- Testing procedures

## Summary

✅ **Completed**:
- Mini-game architecture and base classes
- **Chalices mini-game** implementation (Poisoners vs Testers)
- **Worst Answer mini-game** implementation (Opinion voting)
- **Quick Math mini-game** implementation (Mental math race)
- **Grab More Points mini-game** implementation (Prisoner's dilemma)
- **Pattern Tiles mini-game** implementation (Memory challenge)
- **Playing at a Disadvantage mini-game** implementation (Penalty game, NO eliminations)
- **Playing at a Disadvantage Integration**: Disabled positions connected to trivia answer UI
  - Added `disabled_answer_position` field to Player model
  - Created database migration script
  - Updated mini-game result handling to store disabled positions
  - Modified question broadcast to include disabled positions
  - Frontend answer buttons grey out and disable selected positions
  - CSS styling with strikethrough and diagonal stripes
- Opinion questions module (50+ questions)
- Mini-game manager service with point award system
- Ghost player database schema
- Database migration scripts
- Comprehensive documentation
- Integration guide
- Root README updates
- Frontend UI for all six games

🔄 **Next**:
- Run database migration for disabled_answer_position field
- Test complete flow with all six games
- Test Pattern Tiles two-phase gameplay (memorization + recreation)
- Test Playing at a Disadvantage persistent penalties and disabled UI
- Test all game modes and edge cases
- Add more mini-games
- Deploy and iterate

---

**Status**: Core Implementation Complete - Six Games Fully Implemented and Integrated
**Version**: 1.6
**Date**: 2025-11-18
**Games**: 6 mini-games (Chalices, Worst Answer, Quick Math, Grab More Points, Pattern Tiles, Playing at a Disadvantage)
**Team**: Backend and frontend infrastructure complete
**Note**: Database migration must be run: `python3 backend/migrations/add_disabled_answer_position.py`
