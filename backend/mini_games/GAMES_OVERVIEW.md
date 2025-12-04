# Mini-Games Overview

## Quick Reference

| Game | Duration | Players | Mechanics | Status |
|------|----------|---------|-----------|--------|
| **Chalices** | 45s | 1+ testers | Poison voting & drinking | ✅ Complete |
| **Worst Answer** | 50s | 2+ at-risk | Submit & vote worst answers | ✅ Complete |
| **Quick Math** | 45s | 1+ at-risk | Mental math race | ✅ Complete |
| **Grab More Points** | 30s | 2+ at-risk | Prisoner's dilemma (greed vs cooperation) | ✅ Complete |
| **Pattern Tiles** | 40s | 1+ at-risk | Memory game with tile patterns | ✅ Complete |
| **Playing at a Disadvantage** | 30s | 1+ at-risk | Disable answer position for rest of game (NO eliminations) | ✅ Complete |

---

## Game Details

### 1. Chalices

**Concept**: Medieval poison game - drink from the wrong chalice and you're eliminated!

**Roles**:
- **Poisoners** (correct answerers): Vote on which chalices to poison
- **Testers** (incorrect answerers): Choose which chalice to drink

**Flow**:
1. Setup: Create chalices (max of total players or 3)
2. Poisoners vote on chalices to poison (45s)
3. Testers choose chalices to drink (simultaneous)
4. Resolution: Testers who drank poison are eliminated

**Elimination**: Drink a poisoned chalice = eliminated

**Features**:
- Majority voting determines poisoned chalices
- Random selection if testers don't choose in time
- Can eliminate 0 to all testers

**File**: `chalices.py` (250 lines)

---

### 2. Worst Answer

**Concept**: Submit intentionally bad answers to opinion questions, then vote on the worst!

**Roles**:
- **At-risk players** (incorrect answerers): Submit worst answers
- **Safe players** (correct answerers): Vote only
- **Ghost players**: Vote only

**Flow**:
1. Setup: Random opinion question selected
2. Phase 1 - Submission (30s): At-risk players submit worst answers
3. Phase 2 - Voting (20s): ALL players vote on worst answer
4. Resolution: Player with most votes eliminated

**Elimination**: Receive most votes for "worst answer" = eliminated

**Features**:
- 50+ opinion questions across categories
- Input sanitization (30 chars max, alphanumeric + basic punctuation)
- Two-phase gameplay
- Cannot vote for your own answer
- Tie-breaking via random selection
- Ghost players can vote

**Files**:
- `worst_answer.py` (290 lines)
- `opinion_questions.py` (130 lines, 50+ questions)

**Opinion Question Categories**:
- Entertainment & Pop Culture (karaoke, movies, TV shows)
- Food & Drink (pizza toppings, ice cream, last meals)
- Social Situations (gifts, dates, job interviews)
- Daily Life & Random (pets, smells, chores)

**Example Questions**:
- "What is the worst song to sing for karaoke?"
- "What is the best food as a last meal?"
- "What is the worst excuse for being late?"
- "What is the best superhero power to have?"

---

### 3. Quick Math

**Concept**: Fast-paced mental arithmetic race - answer simple math questions as quickly as possible!

**Roles**:
- **Racers** (varies based on mode): Players competing in the math race
- **Observers** (if applicable): Watch the race unfold

**Two Game Modes**:

**Mode 1 - At-Risk vs At-Risk** (Multiple incorrect answerers):
- All at-risk players compete against each other
- Lowest scorer is eliminated

**Mode 2 - At-Risk vs Safe** (Single incorrect answerer):
- Single at-risk player must beat safe players
- At-risk player must place 1st or be eliminated

**Flow**:
1. Setup: Determine game mode based on player counts
2. Race Phase (45s): Players answer as many math questions as possible
3. Question Request: Players request new questions via button/submit
4. Instant Delivery: Server generates and sends questions immediately
5. Scoring: Each correct answer = 1 point
6. Resolution: Eliminate based on scores and game mode

**Elimination**:
- Mode 1: Lowest scorer eliminated
- Mode 2: At-risk player eliminated if they don't place 1st

**Features**:
- Request/response pattern for instant question delivery
- Simple arithmetic: addition (1-20), subtraction (1-30), multiplication (1-12), division (whole numbers)
- Optimistic UI updates for speed
- Real-time score tracking
- No delay between questions (~100ms)
- Examples: "5 + 12", "8 × 7", "24 ÷ 4", "15 - 8"

**File**: `quick_math.py` (410 lines)

**Math Question Types**:
- **Addition**: 1-20 + 1-20 (e.g., "7 + 14")
- **Subtraction**: 10-30 - 1-15 (e.g., "25 - 9", always positive)
- **Multiplication**: 1-12 × 1-12 (e.g., "6 × 8", times tables)
- **Division**: Guaranteed whole numbers (e.g., "36 ÷ 6")

---

### 4. Grab More Points

**Concept**: Prisoner's dilemma - grab bonus points, but greed has consequences!

**Roles**:
- **At-risk players** (decision makers): Choose how many points to grab (0-1000)
- **Safe players** (observers): Watch and wait

**The Dilemma**:

**Scenario 1 - No One Grabs Points** (Cooperation):
- ✅ Everyone survives!
- No eliminations
- Trust prevails

**Scenario 2 - Some Grab Points** (Mixed):
- ⚠️ Those who took 0 points become ghosts
- Those who grabbed points survive
- Greed pays off, but at a cost

**Scenario 3 - Everyone Grabs Points** (Full Greed):
- ❌ Everyone becomes a ghost!
- Mutual destruction
- Nobody wins

**Flow**:
1. Setup: At-risk players shown rules and decision form
2. Decision Phase (30s): Players enter points to grab (0-1000)
3. Submission: Players submit their choice
4. Resolution: Determine eliminations based on collective choices
5. Point Awards: All grabbed points added to player scores (regardless of elimination)

**Elimination**:
- 0 grabbers → 0 eliminations
- Some grabbers → Non-grabbers eliminated
- All grabbers → All eliminated

**Features**:
- Classic prisoner's dilemma mechanics
- Points ALWAYS added to score (even if eliminated)
- Dynamic button text: "No points thanks" vs "Give me the points!"
- Visual feedback for greedy vs noble choices
- Requires minimum 2 at-risk players for the dilemma to work
- Suspenseful reveal of collective decision

**File**: `grab_more_points.py` (230 lines)

**Strategic Considerations**:
- **Trust**: Will others cooperate?
- **Greed**: Is it worth the risk?
- **Score Gap**: Can you afford to pass up points?
- **Player Count**: More players = harder to predict
- **Game Theory**: Classic Nash equilibrium dilemma

---

### 5. Pattern Tiles

**Concept**: Memory game where players must memorize and recreate a pattern of blue and white tiles!

**Roles**:
- **Competitors** (varies by mode): Players who must memorize and recreate the pattern
- **Observers** (if applicable): Watch the memory challenge unfold

**Two Game Modes**:

**Mode 1 - At-Risk vs At-Risk** (Multiple incorrect answerers):
- All at-risk players compete against each other
- Lowest accuracy percentage eliminated

**Mode 2 - At-Risk vs All** (Single incorrect answerer):
- Single at-risk player competes against everyone (safe and ghost players)
- At-risk player eliminated if anyone scores higher accuracy

**Flow**:
1. Setup: Generate random 4x4 pattern of blue and white tiles
2. Memorization Phase (10s): Pattern shown on TV screen for all to study
3. Pattern Hidden: TV pattern disappears
4. Recreation Phase (30s): Players get blank (all white) grids
5. Players click tiles to toggle between white and blue
6. Submit grids (early or on timeout)
7. Calculate accuracy percentages (matching tiles / total tiles)
8. Determine elimination based on scores and game mode

**Elimination**:
- Mode 1: Lowest accuracy percentage eliminated
- Mode 2: At-risk player eliminated if they don't have highest accuracy

**Features**:
- 4x4 grid with blue and white tiles separated by black borders
- Two-phase gameplay: memorization (10s) → recreation (30s)
- Click white tile → turns blue
- Click blue tile → turns white
- Submit button for early submission
- Accuracy calculated as percentage of matching tiles
- Visual grid display on both TV (pattern) and mobile (player grid)
- Observer screen for non-competing players
- Random pattern generation (roughly 50/50 blue/white)
- Examples: Pattern might be checkered, random, or any combination

**File**: `pattern_tiles.py` (402 lines)

**Memory Challenge Tips**:
- Look for patterns (rows, columns, diagonals)
- Group tiles mentally (e.g., "top-left quadrant mostly blue")
- Count blue vs white tiles for overall balance
- Focus on memorable features or symmetries

---

### 6. Playing at a Disadvantage

**Concept**: Penalty game where players choose which answer position they'll be unable to select for the rest of the game!

**Roles**:
- **At-risk players** (decision makers): Choose an answer position to disable permanently
- **Safe players** (observers): Watch the strategic choices

**Unique Feature**:
- **NO ELIMINATIONS** - This is a penalty game, not an elimination game!
- Disabled position persists for ALL remaining trivia questions
- Even if you know the disabled position is correct, you can't select it

**Flow**:
1. Setup: At-risk players shown the rules and consequences
2. Selection Phase (30s): Players choose position 1, 2, 3, or 4 to disable
3. Submission: Players submit their choice
4. Results: Show which position each player disabled
5. Penalty Applied: Disabled positions carry forward to all future questions
6. Game Continues: NO players eliminated, everyone survives with disadvantage

**Strategic Considerations**:
- **Position 1 & 2**: Often contain correct answers - risky to disable
- **Position 3**: Moderate risk
- **Position 4**: Safer choice, but still a significant disadvantage
- **No Undo**: Choice is permanent for entire game
- **Future Questions**: Must remember which position you disabled

**Consequences**:
- Disabled answer position greyed out in future trivia questions
- Cannot click or select that position
- Must answer from remaining 3 positions only
- Permanent handicap until game ends

**File**: `playing_at_disadvantage.py` (280 lines)

**Strategy Tips**:
- Consider your trivia knowledge - are you good at eliminating obviously wrong answers?
- Think about common answer patterns in the game
- Balance immediate survival vs. long-term handicap
- If timeout occurs, random position is selected for you

---

## Security Features

### Input Validation

**Worst Answer**:
- Maximum 30 characters
- Regex pattern: `^[a-zA-Z0-9\s.,!?\'-]+$`
- Prevents: SQL injection, XSS, special character exploits
- Only allows: letters, numbers, spaces, basic punctuation (.,!?'-)

**Chalices**:
- Integer validation for chalice selection
- Range checking (0 to num_chalices-1)
- Player ID validation

**Quick Math**:
- Integer validation for answers
- Question ID validation
- Player role verification (only racers can answer)
- Type checking for numeric inputs

**Grab More Points**:
- Integer validation for point values
- Range validation (0-1000 points)
- Player role verification (only at-risk can submit)
- Type checking for numeric inputs

**Pattern Tiles**:
- Grid validation (must be 4x4 array)
- Cell validation (only 0 or 1 values allowed)
- Array structure validation (proper nested lists)
- Player role verification (only competitors can submit)
- Type checking for grid structure

**Playing at a Disadvantage**:
- Integer validation for position selection
- Range validation (1-4 only)
- Player role verification (only at-risk can submit)
- Type checking for numeric inputs
- Random assignment on timeout (failsafe)

---

## Game Selection Algorithm

The `MiniGameManager` automatically selects appropriate games based on player counts:

```python
def select_mini_game(at_risk_count, safe_count):
    eligible_games = [
        game for game in MINI_GAMES.values()
        if at_risk_count >= game.min_players
    ]
    return random.choice(eligible_games)
```

**Game requirements**:
- Chalices: Minimum 1 at-risk player
- Worst Answer: Minimum 2 at-risk players (requires voting)
- Quick Math: Minimum 1 at-risk player
- Grab More Points: Minimum 2 at-risk players (requires dilemma)
- Pattern Tiles: Minimum 1 at-risk player
- Playing at a Disadvantage: Minimum 1 at-risk player (NO eliminations)
- All games support any number of safe players
- Ghost players can vote in Worst Answer only

---

## Integration Points

### WebSocket Messages

**Game Start**:
```json
{
    "type": "mini_game_start",
    "game_name": "Chalices" | "Worst Answer" | "Quick Math" | "Grab More Points" | "Pattern Tiles" | "Playing at a Disadvantage",
    "description": "...",
    "timeout": 30 | 45 | 50,
    "setup": { /* game-specific setup */ }
}
```

**Player Action - Chalices**:
```json
{
    "type": "mini_game_action",
    "action": {
        "type": "vote_chalice" | "choose_chalice",
        "chalice": 0-N
    }
}
```

**Player Action - Worst Answer (Submission)**:
```json
{
    "type": "mini_game_action",
    "action": {
        "type": "submit_answer",
        "answer": "Happy Birthday"
    }
}
```

**Player Action - Worst Answer (Voting)**:
```json
{
    "type": "mini_game_action",
    "action": {
        "type": "vote",
        "voted_for": 123
    }
}
```

**Player Action - Quick Math (Request Question)**:
```json
{
    "type": "mini_game_action",
    "action": {
        "type": "request_question"
    }
}
```

**Player Action - Quick Math (Submit Answer)**:
```json
{
    "type": "mini_game_action",
    "action": {
        "type": "answer",
        "question_id": 0,
        "answer": 12
    }
}
```

**Quick Math Question Delivery**:
```json
{
    "type": "mini_game_question",
    "player_id": 123,
    "question": {
        "question_id": 0,
        "question": "7 + 14",
        "answer": 21,
        "timestamp": 1234567890
    }
}
```

**Player Action - Grab More Points**:
```json
{
    "type": "mini_game_action",
    "action": {
        "type": "submit_points",
        "points": 0-1000
    }
}
```

**Player Action - Pattern Tiles**:
```json
{
    "type": "mini_game_action",
    "action": {
        "type": "submit_grid",
        "grid": [[0,1,0,1], [1,0,1,0], [0,1,0,1], [1,0,1,0]]
    }
}
```

**Player Action - Playing at a Disadvantage**:
```json
{
    "type": "mini_game_action",
    "action": {
        "type": "select_position",
        "position": 1-4
    }
}
```

**Game Results**:
```json
{
    "type": "mini_game_results",
    "eliminated": [player_ids],
    "survivors": [player_ids],
    "game_data": { /* game-specific results */ }
}
```

---

## Timeout Behavior

### Chalices (45 seconds)
- **Poisoners don't vote**: Random chalices poisoned
- **Testers don't choose**: Random chalices assigned

### Worst Answer (50 seconds total)
- **Phase 1 - Submission (30s)**: Non-submitters get "..." as answer
- **Phase 2 - Voting (20s)**: Resolve with current votes
- **If no votes**: Random at-risk player eliminated

### Quick Math (45 seconds)
- **No participation**: Random at-risk player eliminated
- **Racing phase ends**: Resolve with current scores
- **Tie for lowest**: Random selection among tied players

### Grab More Points (30 seconds)
- **No submission**: Treated as taking 0 points (no grab)
- **Partial submissions**: Resolve with submitted values
- **Points always awarded**: Even on timeout

### Pattern Tiles (40 seconds total)
- **Memorization phase (10s)**: Pattern shown to all players
- **Recreation phase (30s)**: Players recreate pattern on their grids
- **No submission**: Empty grid (all white) used, resulting in accuracy based on pattern
- **Partial completion**: Grid in current state used for accuracy calculation
- **Accuracy scoring**: Compared against original pattern for percentage match

### Playing at a Disadvantage (30 seconds)
- **No selection**: Random position (1-4) assigned automatically
- **Partial selections**: Resolve with submitted selections
- **NO eliminations**: All players survive regardless of timeout
- **Penalty applied**: Disabled positions persist for all future questions
- **Failsafe**: Random assignment ensures all players get a disadvantage

---

## Future Game Ideas

Potential mini-games to implement:

1. **Lightning Round** - Quick trivia question, fastest correct answer survives
2. **Rock Paper Scissors** - Tournament-style elimination
3. **Hot Potato** - Pass token, random explosion timer
4. **Memory Match** - Match pairs, fewest matches eliminated
5. **Trivia Duel** - Head-to-head quick questions
6. **Sabotage** - Safe players assign tasks to at-risk players
7. **Auction** - Bid points for immunity
8. **Word Chain** - Continue word chain, first to break eliminated
9. **Number Guess** - Closest to random number survives
10. **Drawing Challenge** - Draw prompt, worst drawing eliminated

---

## Testing Mini-Games

### Unit Tests Required

**Chalices**:
- [ ] Setup with various player counts
- [ ] Poisoner voting (majority, tie)
- [ ] Tester choices
- [ ] Poison resolution logic
- [ ] Timeout handling

**Worst Answer**:
- [ ] Setup with opinion question
- [ ] Answer submission validation
- [ ] Phase transition (submission → voting)
- [ ] Vote counting
- [ ] Tie-breaking
- [ ] Input sanitization
- [ ] Timeout in both phases

**Quick Math**:
- [ ] Setup with various player counts (at-risk vs at-risk, at-risk vs safe)
- [ ] Question generation (all 4 operations)
- [ ] Answer validation and scoring
- [ ] Question request/response flow
- [ ] Timeout handling
- [ ] Elimination logic for both game modes
- [ ] Tie-breaking for lowest score

**Grab More Points**:
- [ ] Setup with 2+ at-risk players
- [ ] Point submission validation (0-1000 range)
- [ ] Scenario 1: No one takes points (all survive)
- [ ] Scenario 2: Some take points (non-grabbers eliminated)
- [ ] Scenario 3: All take points (all eliminated)
- [ ] Point award system (always adds points)
- [ ] Timeout handling (default to 0 points)
- [ ] Dynamic button text updates

### Integration Tests Required

- [ ] Full game flow with all four games
- [ ] WebSocket message handling
- [ ] Database ghost player updates
- [ ] Multiple players concurrent actions
- [ ] Edge cases (1 player, all timeout, etc.)
- [ ] Quick Math rapid question/answer cycles
- [ ] Grab More Points point award system
- [ ] Grab More Points prisoner's dilemma scenarios

---

## Performance Considerations

**Game Duration Impact**:
- Standard question: 30 seconds
- Chalices mini-game: 45 seconds
- Worst Answer mini-game: 50 seconds
- Quick Math mini-game: 45 seconds
- Grab More Points mini-game: 30 seconds
- Pattern Tiles mini-game: 40 seconds
- Playing at a Disadvantage mini-game: 30 seconds
- **Total per round**: ~60-80 seconds (question + mini-game)

**Memory Usage**:
- Active mini-game state stored per room
- Cleaned up after resolution
- Player actions tracked until game complete

**Database Operations**:
- Ghost player updates: 1 transaction per resolution
- Batch player updates for efficiency
- Indexed queries on `is_ghost` field

---

## File Structure

```
backend/mini_games/
├── __init__.py                     # Game registry
├── base_mini_game.py               # Abstract base class
├── chalices.py                     # Chalices game implementation
├── worst_answer.py                 # Worst Answer game implementation
├── quick_math.py                   # Quick Math game implementation
├── grab_more_points.py             # Grab More Points game implementation
├── pattern_tiles.py                # Pattern Tiles game implementation
├── playing_at_disadvantage.py      # Playing at a Disadvantage game implementation
├── opinion_questions.py            # Opinion questions database
├── README.md                       # Detailed documentation
└── GAMES_OVERVIEW.md               # This file
```

---

**Last Updated**: 2025-11-18
**Version**: 1.5
**Games Available**: 6 (Chalices, Worst Answer, Quick Math, Grab More Points, Pattern Tiles, Playing at a Disadvantage)
**Total Lines of Code**: ~2,800 lines
