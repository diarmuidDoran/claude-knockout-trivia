# Mini-Games System

## Overview

Mini-games are elimination games played between trivia questions. Players who answered incorrectly participate in a mini-game that determines who gets eliminated and becomes a "ghost player".

## Quick Start

### Game Flow
```
Question (30s) → Results → Mini-Game (30-60s) → Eliminations → Ghost Players → Next Question
```

### Ghost Players
- Eliminated players become "ghosts"
- Can continue answering questions
- Earn points but cannot win
- Marked visually in the UI

## Available Mini-Games (6 Total)

### 1. Chalices
Poisoners (correct answers) choose which chalices to poison.
Testers (incorrect answers) choose which chalice to drink.
Drink poison = eliminated!

**Timeout**: 45 seconds
**Min Players**: 1 tester
**Eliminates**: Multiple (anyone who drinks poison)
**File**: [chalices.py](chalices.py)

### 2. Worst Answer
At-risk players submit worst answers to opinion questions.
All players (safe, at-risk, ghosts) vote on the worst answer.
Most votes = eliminated!

**Timeout**: 30s submission + 30s voting (60s total)
**Min Players**: 2 at-risk players
**Eliminates**: 1 player (most votes)
**File**: [worst_answer.py](worst_answer.py)
**Questions**: [opinion_questions.py](opinion_questions.py) (50+ questions)

### 3. Quick Math
At-risk players compete in a fast-paced mental math race.
Answer simple arithmetic questions (2-digit numbers max) as fast as possible.
Lowest scorer or at-risk player who doesn't place 1st = eliminated!

**Timeout**: 45 seconds
**Min Players**: 1 at-risk player
**Eliminates**: 1 player (lowest score among at-risk)
**File**: [quick_math.py](quick_math.py)
**Modes**: At-risk vs at-risk OR at-risk vs safe players

### 4. Grab More Points
Prisoner's dilemma game where at-risk players decide to grab bonus points.
Points are ALWAYS added, but greed has consequences!
If anyone takes points, those who don't become ghosts!

**Timeout**: 30 seconds
**Min Players**: 2 at-risk players
**Eliminates**: Multiple (based on collective choices)
**File**: [grab_more_points.py](grab_more_points.py)
**Special**: Points awarded regardless of elimination outcome

### 5. Pattern Tiles
Memory game where at-risk players memorize a 4x4 grid pattern for 10 seconds,
then must recreate it from memory. Lowest accuracy = eliminated!

**Timeout**: 10s memorization + 30s recreation (40s total)
**Min Players**: 1 at-risk player
**Eliminates**: 1 player (lowest accuracy)
**File**: [pattern_tiles.py](pattern_tiles.py)

### 6. Playing at a Disadvantage
Penalty mini-game with NO eliminations. At-risk players must choose which
answer position (1-4) will be permanently disabled for the rest of the game.

**Timeout**: 30 seconds
**Min Players**: 1 at-risk player
**Eliminates**: None (permanent handicap instead)
**File**: [playing_at_disadvantage.py](playing_at_disadvantage.py)
**Special**: Chosen position cannot be selected in future questions

## Files

- `base_mini_game.py` - Abstract base class for all mini-games
- `chalices.py` - Chalices (Poisoners vs Testers)
- `worst_answer.py` - Worst Answer voting game
- `quick_math.py` - Quick Math race
- `grab_more_points.py` - Prisoner's dilemma game
- `pattern_tiles.py` - Memory pattern recreation
- `playing_at_disadvantage.py` - Permanent answer position penalty
- `opinion_questions.py` - Opinion questions for Worst Answer
- `__init__.py` - Game registry and exports

## Creating a New Mini-Game

1. Create a new file inheriting from `BaseMiniGame`
2. Implement required methods:
   - `name` property
   - `description` property
   - `min_players` property
   - `max_eliminates` property
   - `setup()` - Initialize game state
   - `process_player_action()` - Handle player inputs
   - `can_resolve()` - Check if game can end
   - `resolve()` - Determine eliminations
   - `handle_timeout()` - Handle time expiry
3. Register in `__init__.py`
4. Add frontend UI in `frontend/js/mini-games.js`

## WebSocket Events

- `mini_game_start` - Sent when mini-game begins
- `mini_game_phase_change` - Sent when phase changes (e.g., submission → voting)
- `mini_game_action` - Sent/received for player actions
- `mini_game_result` - Sent when mini-game ends with eliminations

---

**Last Updated**: 2025-11-23
