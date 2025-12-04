# Playing at a Disadvantage Integration Summary

**Date**: 2025-11-18
**Status**: ✅ Complete
**Version**: 1.6

## Overview

This document summarizes the integration of the "Playing at a Disadvantage" mini-game with the trivia answer UI. The integration ensures that when players select a disabled answer position (1-4) in the mini-game, that position remains disabled (greyed out and unclickable) for all remaining trivia questions.

---

## What Was Implemented

### 1. Database Schema Changes

**File**: [backend/app/models/models.py](backend/app/models/models.py#L42)

Added a new field to the `Player` model:

```python
disabled_answer_position = Column(Integer, nullable=True)  # Answer position disabled (1-4) from Playing at a Disadvantage
```

**Purpose**: Store which answer position (1, 2, 3, or 4) is permanently disabled for each player.

### 2. Database Migration

**File**: [backend/migrations/add_disabled_answer_position.py](backend/migrations/add_disabled_answer_position.py)

Created migration script to add the new column to existing databases.

**To Run**:
```bash
cd backend
python3 migrations/add_disabled_answer_position.py
```

**Migration Actions**:
- Adds `disabled_answer_position INTEGER NULL` column to `players` table
- Handles existing databases gracefully
- Provides clear success/error messages

### 3. Mini-Game Result Handling

**File**: [backend/app/services/mini_game_manager.py](backend/app/services/mini_game_manager.py#L215-L222)

**Changes**: Added logic to save disabled positions to the database after mini-game resolution.

```python
# Handle Playing at a Disadvantage: Update disabled positions
if result.game_data and 'disabled_positions' in result.game_data:
    disabled_positions = result.game_data['disabled_positions']
    for player_id, position in disabled_positions.items():
        player = db.query(Player).filter(Player.id == player_id).first()
        if player:
            player.disabled_answer_position = position
            print(f"[MINI-GAME] Player {player_id} disabled position {position}")
```

**Flow**:
1. Playing at a Disadvantage mini-game resolves
2. Returns `disabled_positions` dict in `game_data`: `{player_id: position}`
3. Manager updates each player's `disabled_answer_position` in database
4. Positions persist for remainder of game

### 4. Question Broadcasting

**File**: [backend/app/services/game_service.py](backend/app/services/game_service.py)

**Changes in `next_question()` method** (Lines 160-166, 192):

```python
# Get all players in this room to include disabled positions
players = db.query(Player).filter(Player.room_id == room.id).all()
disabled_positions = {
    player.id: player.disabled_answer_position
    for player in players
    if player.disabled_answer_position is not None
}

# Include in broadcast
await self.connection_manager.broadcast_to_room(
    room_code,
    {
        "type": "new_question",
        "question": {...},
        "start_time": start_time.isoformat(),
        "disabled_positions": disabled_positions  # NEW
    }
)
```

**Changes in `handle_sync_request()` method** (Lines 338-344, 374):

Same logic added to sync requests for reconnecting players.

**Data Format**:
```json
{
  "type": "new_question",
  "question": {...},
  "disabled_positions": {
    123: 4,  // Player 123 has position 4 disabled
    456: 2   // Player 456 has position 2 disabled
  }
}
```

### 5. Frontend Answer Button Rendering

**File**: [frontend/js/mobile-game.js](frontend/js/mobile-game.js#L30-L56)

**Changes in `handleNewQuestion()` function**:

```javascript
// Get disabled position for this player (from Playing at a Disadvantage mini-game)
const disabledPositions = data.disabled_positions || {};
const myDisabledPosition = disabledPositions[playerId];

// Display answer options
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
```

**Behavior**:
- Checks if current player has a disabled position
- If position matches option order (1-4), adds `disabled-position` class
- Disables button (prevents clicking)
- Adds 🚫 emoji visual indicator
- Adds tooltip explaining why it's disabled

### 6. CSS Styling

**File**: [frontend/css/game-styles.css](frontend/css/game-styles.css#L123-L149)

**New Styles**:

```css
/* Disabled position (from Playing at a Disadvantage mini-game) */
.answer-btn.disabled-position {
    background: repeating-linear-gradient(
        45deg,
        #f0f0f0,
        #f0f0f0 10px,
        #e0e0e0 10px,
        #e0e0e0 20px
    );
    border-color: #999;
    color: #666;
    cursor: not-allowed;
    opacity: 0.5;
    text-decoration: line-through;
}

.answer-btn.disabled-position:hover {
    transform: none;
    box-shadow: none;
    background: repeating-linear-gradient(
        45deg,
        #f0f0f0,
        #f0f0f0 10px,
        #e0e0e0 10px,
        #e0e0e0 20px
    );
}
```

**Visual Effects**:
- Diagonal striped background (grey)
- Strikethrough text
- 50% opacity
- `not-allowed` cursor
- No hover effects
- Clear visual distinction from active buttons

---

## Data Flow

### 1. During Mini-Game

```
1. Playing at a Disadvantage mini-game starts
2. At-risk players select position (1-4)
3. Mini-game resolves with NO eliminations
4. Returns result with disabled_positions: {player_id: position}
```

### 2. After Mini-Game Resolution

```
5. MiniGameManager.resolve_mini_game() extracts disabled_positions
6. For each player_id, position pair:
   - Query Player from database
   - Set player.disabled_answer_position = position
7. Database commit (positions now persisted)
```

### 3. For Every Future Question

```
8. GameService.next_question() loads question
9. Queries all players in room
10. Builds disabled_positions dict from player.disabled_answer_position
11. Broadcasts to all clients with disabled_positions in message
```

### 4. Frontend Rendering

```
12. Mobile client receives new_question event
13. Extracts disabled_positions from message
14. Looks up current player's disabled position
15. For each answer button:
    - If option.order == myDisabledPosition:
      - Add 'disabled-position' class
      - Set disabled = true
      - Add 🚫 emoji prefix
      - Add tooltip
    - Else:
      - Normal clickable button
16. Render buttons with disabled state
```

---

## Example Usage

### Scenario

1. **Question 3**: Player "Alice" (ID: 123) answers incorrectly
2. **Mini-Game**: Playing at a Disadvantage starts
3. **Alice's Choice**: Selects position 4 (decides to disable 4th answer)
4. **Results**: NO eliminations, Alice survives with disadvantage
5. **Database**: `alice.disabled_answer_position = 4` saved
6. **Question 4**:
   - Server broadcasts question with `disabled_positions: {123: 4}`
   - Alice's phone receives question
   - Answer buttons render:
     - Position 1: ✅ Clickable (normal)
     - Position 2: ✅ Clickable (normal)
     - Position 3: ✅ Clickable (normal)
     - Position 4: 🚫 **Disabled** (greyed, strikethrough, unclickable)
7. **Question 5, 6, 7...**: Same disabled state persists
8. **Game End**: Disadvantage applied to all questions after mini-game

---

## Technical Details

### Backend Integration Points

1. **Model Layer** (`models.py`):
   - Added nullable integer field for position storage
   - Field accepts values 1-4 or NULL

2. **Mini-Game Manager** (`mini_game_manager.py`):
   - Checks for `disabled_positions` in result.game_data
   - Iterates through player_id: position pairs
   - Updates database with disabled positions

3. **Game Service** (`game_service.py`):
   - Queries players on every question
   - Builds disabled_positions dict
   - Includes in both broadcast and sync messages

### Frontend Integration Points

1. **Game Logic** (`mobile-game.js`):
   - Extracts disabled_positions from question data
   - Looks up player's specific disabled position
   - Applies disabled state during button creation

2. **Styling** (`game-styles.css`):
   - Visual feedback with striped background
   - Clear disabled state (no hover effects)
   - Accessibility (cursor, tooltip, strikethrough)

### WebSocket Message Format

**New Field in `new_question` Event**:

```json
{
  "type": "new_question",
  "question": {
    "id": 42,
    "text": "What is the capital of France?",
    "category": "geography",
    "time_limit": 30,
    "options": [
      {"id": 1, "text": "London", "order": 1},
      {"id": 2, "text": "Paris", "order": 2},
      {"id": 3, "text": "Berlin", "order": 3},
      {"id": 4, "text": "Madrid", "order": 4}
    ]
  },
  "start_time": "2025-11-18T12:34:56.789Z",
  "disabled_positions": {
    "123": 4,
    "456": 2
  }
}
```

**Interpretation**:
- Player 123: Position 4 disabled (can't select "Madrid")
- Player 456: Position 2 disabled (can't select "Paris")
- All other players: All positions enabled

---

## Testing Checklist

### Database Migration
- [ ] Run migration script successfully
- [ ] Verify column added to players table
- [ ] Check existing players have NULL values
- [ ] Confirm migration is idempotent (can run multiple times)

### Mini-Game Flow
- [ ] Play Playing at a Disadvantage mini-game
- [ ] Select different positions (1, 2, 3, 4)
- [ ] Verify positions saved to database
- [ ] Check no eliminations occur
- [ ] Confirm all players get disadvantage

### Trivia UI Integration
- [ ] Start new question after mini-game
- [ ] Verify disabled position is greyed out
- [ ] Confirm disabled button is unclickable
- [ ] Check tooltip appears on hover
- [ ] Verify 🚫 emoji shows on button

### Persistence
- [ ] Play multiple questions after mini-game
- [ ] Confirm disabled position persists across all questions
- [ ] Verify different players have different disabled positions
- [ ] Check disabled state until game ends

### Edge Cases
- [ ] Player with no disabled position (normal gameplay)
- [ ] All players have different disabled positions
- [ ] Player reconnects after mini-game (sync request)
- [ ] Disabled position matches correct answer (can't select correct answer)

### Visual & UX
- [ ] Striped background displays correctly
- [ ] Strikethrough text is readable
- [ ] Opacity makes it clearly disabled
- [ ] No hover effects on disabled buttons
- [ ] Other buttons remain fully functional

---

## Files Modified

### Backend
1. **[backend/app/models/models.py](backend/app/models/models.py)** - Added `disabled_answer_position` field (line 42)
2. **[backend/migrations/add_disabled_answer_position.py](backend/migrations/add_disabled_answer_position.py)** - NEW migration script
3. **[backend/app/services/mini_game_manager.py](backend/app/services/mini_game_manager.py)** - Added disabled position handling (lines 215-222)
4. **[backend/app/services/game_service.py](backend/app/services/game_service.py)** - Added disabled positions to broadcasts (lines 160-166, 192, 338-344, 374)

### Frontend
1. **[frontend/js/mobile-game.js](frontend/js/mobile-game.js)** - Added disabled position rendering (lines 30-56)
2. **[frontend/css/game-styles.css](frontend/css/game-styles.css)** - Added disabled position styling (lines 123-149)

### Documentation
1. **[MINI_GAME_IMPLEMENTATION.md](MINI_GAME_IMPLEMENTATION.md)** - Updated status, version, next steps
2. **[PLAYING_AT_DISADVANTAGE_INTEGRATION.md](PLAYING_AT_DISADVANTAGE_INTEGRATION.md)** - THIS FILE (NEW)

---

## Next Steps

1. **Run Migration**: Execute `python3 backend/migrations/add_disabled_answer_position.py`
2. **Test End-to-End**: Play full game with Playing at a Disadvantage mini-game
3. **Verify Persistence**: Confirm disabled positions persist across multiple questions
4. **Edge Case Testing**: Test all edge cases listed above
5. **User Acceptance**: Gather feedback on visual design and UX

---

## Known Limitations

None currently - integration is complete and ready for testing.

---

## Future Enhancements

1. **TV Display**: Show which positions are disabled for each player on TV screen
2. **Statistics**: Track how often each position gets disabled
3. **Analytics**: Measure impact of disadvantage on player performance
4. **Visual Options**: Allow customization of disabled button styling
5. **Reset Option**: Admin ability to clear disabled positions mid-game

---

## Support

For issues or questions about this integration:
1. Check WebSocket messages in browser console
2. Verify database migration ran successfully
3. Confirm player has `disabled_answer_position` set in database
4. Review server logs for mini-game resolution

---

**Integration Status**: ✅ Complete
**Version**: 1.6
**Date**: 2025-11-18
**Author**: Claude Code Integration
**Next Action**: Run database migration and test
