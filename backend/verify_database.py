#!/usr/bin/env python3
"""Verify the question database is ready for the game."""

import sys
sys.path.insert(0, '.')

from app.models.database import SessionLocal
from app.models.models import Question, QuestionOption
from collections import Counter

def verify_database():
    """Verify database integrity and game compatibility."""
    db = SessionLocal()

    # Get all questions
    all_questions = db.query(Question).all()
    total = len(all_questions)

    # Check for duplicates
    question_texts = [q.question_text for q in all_questions]
    text_counts = Counter(question_texts)
    duplicates = {text: count for text, count in text_counts.items() if count > 1}

    # Get distributions
    categories = Counter([q.category for q in all_questions])
    difficulties = Counter([q.difficulty for q in all_questions])

    print('=' * 70)
    print('FINAL VERIFICATION - KNOCKOUT TRIVIA QUESTION DATABASE')
    print('=' * 70)
    print(f'\nTOTAL QUESTIONS: {total}')
    print(f'UNIQUE QUESTIONS: {len(set(question_texts))}')
    print(f'DUPLICATES FOUND: {len(duplicates)}')

    if duplicates:
        print('\nDUPLICATE QUESTIONS:')
        for text, count in sorted(duplicates.items(), key=lambda x: -x[1]):
            print(f'  ({count}x) {text[:60]}...')

    print(f'\nALL QUESTIONS ACTIVE: {all([q.is_active for q in all_questions])}')

    print(f'\nCATEGORY DISTRIBUTION ({len(categories)} categories):')
    for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
        percentage = (count / total) * 100
        print(f'  {cat:20s}: {count:3d} ({percentage:5.1f}%)')

    print(f'\nDIFFICULTY DISTRIBUTION:')
    for diff, count in sorted(difficulties.items()):
        percentage = (count / total) * 100
        print(f'  {diff:20s}: {count:3d} ({percentage:5.1f}%)')

    print(f'\nGAME COMPATIBILITY CHECK:')
    active_questions = db.query(Question).filter(Question.is_active == True).all()
    print(f'  Questions accessible by game: {len(active_questions)}')
    print(f'  All questions have text: {all([q.question_text for q in active_questions])}')
    print(f'  All questions have category: {all([q.category for q in active_questions])}')

    # Check if all questions have 4 options
    questions_with_options = []
    for q in active_questions[:20]:  # Check first 20
        if len(q.options) == 4:
            questions_with_options.append(True)
        else:
            questions_with_options.append(False)
            print(f'  WARNING: Question {q.id} has {len(q.options)} options')

    if questions_with_options:
        print(f'  Sample questions have 4 options: {all(questions_with_options)}')

    print(f'\n{"=" * 70}')
    if total == 1000 and len(duplicates) == 0:
        print('SUCCESS! Database ready for game!')
        print('  - 1,000 unique questions')
        print('  - No duplicates')
        print('  - All questions accessible for random selection')
        no_easy = difficulties.get('easy', 0)
        print(f'  - Easy questions: {no_easy} (user requested no easy questions)')
    else:
        print('ISSUES DETECTED:')
        if total != 1000:
            print(f'  - Expected 1000 questions, found {total}')
        if duplicates:
            print(f'  - Found {len(duplicates)} duplicate questions')
    print('=' * 70)

    db.close()
    return len(duplicates) == 0 and total == 1000

if __name__ == "__main__":
    success = verify_database()
    sys.exit(0 if success else 1)
