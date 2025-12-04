# Mini-Game Integration Guide

This guide explains how to integrate the mini-game system into the game service for the Knockout Trivia game.

## Overview

The mini-game system runs between trivia questions to eliminate players who answered incorrectly. The flow is:

```
Question → Results → Mini-Game → Eliminations → Next Question
```

## Quick Setup

### 1. Run Database Migration

```bash
cd backend
python migrations/add_ghost_player_fields.py
```

This adds `is_ghost` and `eliminated_at` fields to the `players` table.

### 2. Import Mini-Game Manager

In `app/services/game_service.py`:

```python
from app.services.mini_game_manager import MiniGameManager

class GameService:
    def __init__(self, connection_manager: ConnectionManager):
        self.connection_manager = connection_manager
        self.mini_game_manager = MiniGameManager()  # Add this
        # ... rest of init
```

## Integration Points

### Point 1: After Question Results

After showing question results, determine which players answered correctly/incorrectly and start a mini-game.

**Location**: After `show_question_results()` or similar method

**Code**:
```python
async def handle_question_results(self, room_code: str, question_id: int):
    db = SessionLocal()
    try:
        # Get all answers for this question
        answers = db.query(Answer).filter(
            Answer.question_id == question_id
        ).join(Player).filter(
            Player.room.has(code=room_code),
            Player.is_ghost == False  # Only living players
        ).all()

        # Separate correct and incorrect answers
        correct_players = []
        incorrect_players = []

        for answer in answers:
            if answer.selected_option.is_correct:
                correct_players.append(answer.player_id)
            else:
                incorrect_players.append(answer.player_id)

        # Show results first
        await self.connection_manager.broadcast_to_room(
            room_code,
            {
                "type": "question_results",
                "correct_players": correct_players,
                "incorrect_players": incorrect_players,
                # ... other result data
            }
        )

        # Wait for players to see results
        await asyncio.sleep(3)

        # Start mini-game if there are incorrect players
        if incorrect_players:
            await self.start_mini_game(room_code, incorrect_players, correct_players)
        else:
            # Everyone got it right, proceed to next question
            await self.next_question(room_code)

    finally:
        db.close()
```

### Point 2: Start Mini-Game

```python
async def start_mini_game(
    self,
    room_code: str,
    at_risk_players: List[int],
    safe_players: List[int]
):
    """Start a mini-game for elimination."""
    total_living = len(at_risk_players) + len(safe_players)

    # Start mini-game (random selection)
    mini_game_data = self.mini_game_manager.start_mini_game(
        room_code=room_code,
        at_risk_players=at_risk_players,
        safe_players=safe_players,
        total_players=total_living
        # game_name="chalices"  # Optional: specify game
    )

    # Broadcast to all players
    await self.connection_manager.broadcast_to_room(
        room_code,
        mini_game_data
    )

    # Start timeout timer
    asyncio.create_task(
        self.check_mini_game_timeout(room_code)
    )
```

### Point 3: Handle Mini-Game Actions

Add a new message type handler in `handle_websocket_message()`:

```python
async def handle_websocket_message(self, room_code: str, player_id: str, message: str):
    try:
        data = json.loads(message)
        message_type = data.get("type")

        # ... existing handlers ...

        elif message_type == "mini_game_action":
            await self.handle_mini_game_action(room_code, player_id, data)

    except json.JSONDecodeError:
        # ... error handling
```

**Implementation**:
```python
async def handle_mini_game_action(
    self,
    room_code: str,
    player_id: str,
    data: Dict[str, Any]
):
    """Handle a player's action in the mini-game."""
    try:
        player_id_int = int(player_id)
    except ValueError:
        return

    action = data.get("action")
    if not action:
        return

    # Process action
    success = await self.mini_game_manager.process_player_action(
        room_code,
        player_id_int,
        action
    )

    if not success:
        await self.connection_manager.send_personal_message(
            {
                "type": "error",
                "message": "Invalid mini-game action"
            },
            room_code,
            player_id
        )
        return

    # Notify room that player acted
    await self.connection_manager.broadcast_to_room(
        room_code,
        {
            "type": "mini_game_player_action",
            "player_id": player_id_int,
            "action_received": True
        }
    )

    # Check if ready to resolve
    if self.mini_game_manager.can_resolve(room_code):
        await self.resolve_mini_game(room_code)
```

### Point 4: Resolve Mini-Game

```python
async def resolve_mini_game(self, room_code: str):
    """Resolve the mini-game and eliminate players."""
    db = SessionLocal()
    try:
        # Resolve mini-game
        result = self.mini_game_manager.resolve_mini_game(
            room_code,
            db,
            force=False
        )

        if not result.success:
            await self.connection_manager.broadcast_to_room(
                room_code,
                {
                    "type": "error",
                    "message": result.error_message or "Mini-game failed"
                }
            )
            return

        # Get player names for eliminated players
        eliminated_players = db.query(Player).filter(
            Player.id.in_(result.eliminated_player_ids)
        ).all()

        # Broadcast results
        await self.connection_manager.broadcast_to_room(
            room_code,
            {
                "type": "mini_game_results",
                "eliminated": [
                    {
                        "player_id": p.id,
                        "player_name": p.name
                    }
                    for p in eliminated_players
                ],
                "survivors": result.survivors,
                "game_data": result.game_data
            }
        )

        # Wait for players to see results
        await asyncio.sleep(5)

        # Check if game should end (only 1 or 0 living players)
        living_count = db.query(Player).filter(
            Player.room.has(code=room_code),
            Player.is_ghost == False,
            Player.is_connected == True
        ).count()

        if living_count <= 1:
            await self.end_game(room_code)
        else:
            # Continue to next question
            await self.next_question(room_code)

    finally:
        db.close()
```

### Point 5: Handle Mini-Game Timeout

```python
async def check_mini_game_timeout(self, room_code: str):
    """Check for mini-game timeout and force resolution."""
    # Get timeout duration from mini-game
    mini_game = self.mini_game_manager.get_active_mini_game(room_code)
    if not mini_game:
        return

    timeout = mini_game.get_timeout_seconds()

    # Wait for timeout
    await asyncio.sleep(timeout)

    # Check if still active and not resolved
    if not self.mini_game_manager.can_resolve(room_code):
        db = SessionLocal()
        try:
            # Force resolution with timeout
            result = self.mini_game_manager.resolve_mini_game(
                room_code,
                db,
                force=True  # Handle timeout
            )

            # Broadcast timeout message
            await self.connection_manager.broadcast_to_room(
                room_code,
                {
                    "type": "mini_game_timeout",
                    "message": "Time's up! Players who didn't act were eliminated."
                }
            )

            # Then show results
            await self.connection_manager.broadcast_to_room(
                room_code,
                {
                    "type": "mini_game_results",
                    "eliminated": result.eliminated_player_ids,
                    "survivors": result.survivors,
                    "game_data": result.game_data,
                    "timeout": True
                }
            )

            await asyncio.sleep(5)

            # Continue game
            living_count = db.query(Player).filter(
                Player.room.has(code=room_code),
                Player.is_ghost == False
            ).count()

            if living_count <= 1:
                await self.end_game(room_code)
            else:
                await self.next_question(room_code)

        finally:
            db.close()
```

### Point 6: Update Player Queries

**Update all player queries** to distinguish between living and ghost players:

```python
# Get living players only
living_players = db.query(Player).filter(
    Player.room_id == room_id,
    Player.is_ghost == False
).all()

# Get all players (including ghosts)
all_players = db.query(Player).filter(
    Player.room_id == room_id
).all()

# Get ghost players
ghost_players = db.query(Player).filter(
    Player.room_id == room_id,
    Player.is_ghost == True
).all()
```

### Point 7: Update End Game Logic

Only living players can win:

```python
async def end_game(self, room_code: str):
    db = SessionLocal()
    try:
        # Get winner (last living player or highest score among living)
        winner = db.query(Player).filter(
            Player.room.has(code=room_code),
            Player.is_ghost == False  # Must be living
        ).order_by(
            Player.total_score.desc()
        ).first()

        # Get all players for final leaderboard
        all_players = db.query(Player).filter(
            Player.room.has(code=room_code)
        ).order_by(
            Player.is_ghost.asc(),  # Living players first
            Player.total_score.desc()
        ).all()

        await self.connection_manager.broadcast_to_room(
            room_code,
            {
                "type": "game_ended",
                "winner": {
                    "player_id": winner.id,
                    "player_name": winner.name,
                    "score": winner.total_score
                } if winner else None,
                "leaderboard": [
                    {
                        "player_id": p.id,
                        "player_name": p.name,
                        "score": p.total_score,
                        "is_ghost": p.is_ghost,
                        "rank": idx + 1
                    }
                    for idx, p in enumerate(all_players)
                ]
            }
        )

    finally:
        db.close()
```

## WebSocket Messages

### From Frontend to Backend

**Mini-Game Action**:
```json
{
    "type": "mini_game_action",
    "action": {
        "type": "choose_chalice",  // Game-specific
        "chalice": 2
    }
}
```

### From Backend to Frontend

**Mini-Game Start**:
```json
{
    "type": "mini_game_start",
    "game_name": "Chalices",
    "description": "Poisoners choose...",
    "timeout": 45,
    "setup": { ... },
    "introduction": { ... }
}
```

**Mini-Game Results**:
```json
{
    "type": "mini_game_results",
    "eliminated": [{"player_id": 1, "player_name": "Alice"}],
    "survivors": [2, 3],
    "game_data": { ... }
}
```

## Testing

### 1. Test Mini-Game Selection

```python
manager = MiniGameManager()
game_class = manager.select_mini_game(
    at_risk_count=2,
    safe_count=3
)
assert game_class is not None
```

### 2. Test Full Flow

```python
async def test_mini_game_flow():
    # Start game
    data = manager.start_mini_game(
        "TEST",
        at_risk_players=[1, 2],
        safe_players=[3, 4],
        total_players=4
    )

    # Process actions
    await manager.process_player_action("TEST", 1, {...})
    await manager.process_player_action("TEST", 2, {...})

    # Resolve
    result = manager.resolve_mini_game("TEST", db)
    assert len(result.eliminated_player_ids) >= 0
```

## Troubleshooting

**Issue**: Mini-game doesn't start
- Check that there are incorrect players
- Verify `MiniGameManager` is initialized
- Check logs for errors

**Issue**: Players not eliminated
- Verify database migration ran
- Check `resolve_mini_game` commits to DB
- Ensure `is_ghost` field exists

**Issue**: Game doesn't continue after mini-game
- Check `next_question()` is called
- Verify living player count logic
- Check for asyncio errors

## Summary

1. ✅ Add `MiniGameManager` to GameService
2. ✅ Start mini-game after question results
3. ✅ Handle mini-game actions from players
4. ✅ Resolve mini-game and eliminate players
5. ✅ Handle timeouts
6. ✅ Update player queries for living/ghost
7. ✅ Update end game for living players only

---

**See also**:
- [Mini-Games README](mini_games/README.md) - Complete mini-game documentation
- [Backend README](README.md) - General backend documentation

**Date**: 2025-11-18
