# Question Data Organization

This directory contains trivia questions organized by difficulty level for the Knockout Trivia game.

## File Structure

```
questions_data/
├── __init__.py           # Module initialization and helper functions
├── easy_questions.py     # Easy difficulty questions
├── medium_questions.py   # Medium difficulty questions
├── hard_questions.py     # Hard difficulty questions
├── expert_questions.py   # Expert difficulty questions
└── README.md            # This file
```

## Current Database Status

According to [QUESTIONS_SUMMARY.md](../QUESTIONS_SUMMARY.md):

- **Total Questions**: 1,000
- **Easy**: 85 questions (8.5%)
- **Medium**: 169 questions (16.9%)
- **Hard**: 256 questions (25.6%)
- **Expert**: 489 questions (48.9%)

## Adding New Questions

To add new questions to the game:

1. **Choose the appropriate difficulty file**:
   - `easy_questions.py` - For straightforward, general knowledge questions
   - `medium_questions.py` - For moderately challenging questions
   - `hard_questions.py` - For difficult questions requiring specific knowledge
   - `expert_questions.py` - For very difficult questions requiring specialized knowledge

2. **Add your question** in the following format:

```python
{
    "text": "What is the question?",
    "category": "Category Name",
    "correct": "Correct Answer",
    "wrong": ["Wrong Answer 1", "Wrong Answer 2", "Wrong Answer 3"]
}
```

3. **Available Categories**:
   - Coding
   - Pop Culture
   - Gaming
   - science
   - geography
   - history
   - sports
   - music
   - technology
   - entertainment
   - literature
   - General
   - art
   - D&D
   - general
   - Fandom

4. **Run the seed script**:

```bash
# Add all new questions
python seed_questions.py

# Add only questions from a specific difficulty
python seed_questions.py --difficulty easy
python seed_questions.py --difficulty medium
python seed_questions.py --difficulty hard
python seed_questions.py --difficulty expert

# Check what would be added without actually adding
python seed_questions.py --check-only
```

## Question Guidelines

- **Uniqueness**: Each question text must be unique (duplicates are automatically skipped)
- **Answer Format**: Provide exactly 1 correct answer and 3 wrong answers
- **Time Limit**: All questions use a 30-second time limit
- **Active Status**: All questions are set to active (`is_active = True`) by default

## Example Question

```python
{
    "text": "What is the chemical symbol for gold?",
    "category": "science",
    "correct": "Au",
    "wrong": ["Go", "Gd", "Gl"]
}
```

## Utility Functions

The `__init__.py` file provides helper functions:

```python
from questions_data import get_all_questions, get_questions_by_difficulty

# Get all questions organized by difficulty
all_questions = get_all_questions()

# Get questions for a specific difficulty
easy_questions = get_questions_by_difficulty('easy')
```

## Migration from Old System

This organized structure replaces the previous system of multiple `add_*.py` files:
- ❌ `add_500_questions.py` (deprecated)
- ❌ `add_final_99_questions.py` (deprecated)
- ❌ `add_last_25_questions.py` (deprecated)
- ❌ `add_final_8_questions.py` (deprecated)
- ❌ `add_final_33_unique.py` (deprecated)

Use the new `seed_questions.py` script instead for all question seeding operations.
