# Knockout Trivia - Backend

FastAPI backend for the Knockout Trivia game with WebSocket support for real-time multiplayer gameplay.

## Project Structure

```
backend/
├── app/
│   ├── models/
│   │   ├── database.py      # Database configuration
│   │   └── models.py         # SQLAlchemy models
│   ├── services/
│   │   └── game_service.py   # Game logic and WebSocket handling
│   ├── routers/
│   │   └── ...               # API endpoints
│   └── main.py               # FastAPI application
├── questions_data/           # Organized question data by difficulty
│   ├── easy_questions.py
│   ├── medium_questions.py
│   ├── hard_questions.py
│   ├── expert_questions.py
│   └── README.md
├── seed_questions.py         # Unified question seeding script
├── remove_duplicates.py      # Remove duplicate questions
├── verify_database.py        # Verify database integrity
├── init_db.py                # Initialize database tables
└── QUESTIONS_SUMMARY.md      # Question database documentation
```

## Database

The application uses PostgreSQL with SQLAlchemy ORM.

### Models

- **Room**: Game room/lobby
- **Player**: Player information
- **Question**: Trivia questions
- **QuestionOption**: Multiple choice options
- **Answer**: Player answers

### Question Database

The database contains **1,000 unique trivia questions** organized across:

- **16 Categories**: Coding, Pop Culture, Gaming, Science, Geography, History, Sports, Music, Technology, Entertainment, Literature, General, Art, D&D, Fandom
- **4 Difficulty Levels**:
  - Easy: 85 questions (8.5%)
  - Medium: 169 questions (16.9%)
  - Hard: 256 questions (25.6%)
  - Expert: 489 questions (48.9%)

See [QUESTIONS_SUMMARY.md](QUESTIONS_SUMMARY.md) for detailed information.

## Setup

### Prerequisites

- Python 3.8+
- PostgreSQL

### Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure database connection in `app/models/database.py`

3. Initialize database:
```bash
python init_db.py
```

4. (Optional) Seed questions if starting fresh:
```bash
python seed_questions.py
```

## Running the Server

```bash
python -m uvicorn app.main:app --reload --port 8001
```

The server will be available at http://localhost:8001

## Question Management

### Adding New Questions

1. Add questions to the appropriate difficulty file in `questions_data/`:
   - `easy_questions.py`
   - `medium_questions.py`
   - `hard_questions.py`
   - `expert_questions.py`

2. Run the seed script:
```bash
# Add all new questions
python seed_questions.py

# Add only specific difficulty
python seed_questions.py --difficulty medium

# Check what would be added without actually adding
python seed_questions.py --check-only
```

See [questions_data/README.md](questions_data/README.md) for detailed guidelines.

### Database Maintenance

```bash
# Remove duplicate questions
python remove_duplicates.py

# Verify database integrity
python verify_database.py

# Re-initialize database (WARNING: Deletes all data)
python init_db.py
```

## API Documentation

When the server is running, visit:
- Swagger UI: http://localhost:8001/docs
- ReDoc: http://localhost:8001/redoc

## Game Features

- Real-time multiplayer via WebSocket
- Random question selection (no repeats in same game)
- Per-room question tracking
- 30-second timer per question
- Randomized answer positions (correct answer randomly placed 1-4)
- Scoring system
- Player knockout mechanics
- Ghost player system (eliminated players continue but cannot win)
- 6 elimination mini-games

## Mini-Games System

The game includes 6 elimination mini-games played after each question. See [mini_games/README.md](mini_games/README.md) for detailed documentation.

| Mini-Game | Description | Eliminates |
|-----------|-------------|------------|
| Chalices | Poisoners vs Testers - drink poison = eliminated | Multiple |
| Worst Answer | Submit worst answers, vote on the worst | 1 player |
| Quick Math | Mental math race - lowest score eliminated | 1 player |
| Grab More Points | Prisoner's dilemma - greed has consequences | Multiple |
| Pattern Tiles | Memory game - recreate a 4x4 pattern | 1 player |
| Playing at a Disadvantage | Choose answer position to disable permanently | None (penalty) |

## Architecture

### Game Service

The `GameService` class in `app/services/game_service.py` handles:
- Room management
- Player connections via WebSocket
- Question selection and distribution
- Answer validation
- Scoring and elimination logic
- Game state management

### Question Selection

Questions are randomly selected with the following rules:
- All questions have `is_active = True`
- No question repeats within the same game room
- First question is always easy or medium difficulty
- Subsequent questions can be any difficulty

```python
query = db.query(Question).filter(
    Question.is_active == True,
    ~Question.id.in_(used_ids) if used_ids else True
)

# For first question
if is_first:
    query = query.filter(Question.difficulty.in_(['easy', 'medium']))

question = random.choice(query.all())
```

## Development

### Code Organization

- **Organized Structure**: Questions are organized by difficulty in separate files for easy maintenance
- **Unified Seeding**: Single `seed_questions.py` script handles all question additions
- **No Duplicates**: Automatic duplicate detection prevents redundant questions
- **Type Safety**: SQLAlchemy models provide type checking
- **Documentation**: Comprehensive README files in each module

### Best Practices

1. Always use `seed_questions.py` for adding questions
2. Check for duplicates before committing: `python seed_questions.py --check-only`
3. Verify database integrity after major changes: `python verify_database.py`
4. Keep question format consistent (see questions_data/README.md)
5. Test questions in-game before deploying to production

## Troubleshooting

### Database Connection Issues

- Ensure PostgreSQL is running
- Check database credentials in `app/models/database.py`
- Verify database exists: `psql -l`

### Question Seeding Issues

- Run with `--check-only` first to preview changes
- Check for duplicate questions
- Ensure all questions have required fields (text, category, correct, wrong)

### WebSocket Connection Issues

- Check CORS settings in `app/main.py`
- Verify WebSocket URL in frontend matches backend port
- Check browser console for connection errors

## License

[Your License]

## Contributing

[Contributing Guidelines]
