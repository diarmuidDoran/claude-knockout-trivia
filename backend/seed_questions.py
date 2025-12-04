#!/usr/bin/env python3
"""
Unified script to seed trivia questions into the database.

This script imports questions from the organized question data files:
- questions_data/easy_questions.py
- questions_data/medium_questions.py
- questions_data/hard_questions.py
- questions_data/expert_questions.py

Usage:
    python seed_questions.py                    # Add all questions
    python seed_questions.py --difficulty easy  # Add only easy questions
    python seed_questions.py --difficulty medium # Add only medium questions
    python seed_questions.py --difficulty hard  # Add only hard questions
    python seed_questions.py --difficulty expert # Add only expert questions
    python seed_questions.py --check-only       # Check what would be added without adding
"""

import sys
sys.path.insert(0, '.')

import argparse
import random
from app.models.database import SessionLocal
from app.models.models import Question, QuestionOption
from questions_data import get_all_questions, get_questions_by_difficulty

def add_questions_to_db(questions_data, difficulty, db, check_only=False):
    """Add questions of a specific difficulty to the database."""

    if not questions_data:
        print(f"  No new {difficulty} questions to add")
        return 0, 0

    # Get existing question texts to avoid duplicates
    existing_questions = set([q.question_text for q in db.query(Question).all()])

    added_count = 0
    skipped_count = 0

    for q_data in questions_data:
        # Check for duplicates
        if q_data["text"] in existing_questions:
            skipped_count += 1
            continue

        if check_only:
            print(f"  Would add: {q_data['text'][:60]}...")
            added_count += 1
            continue

        # Create question
        question = Question(
            question_text=q_data["text"],
            category=q_data["category"],
            difficulty=difficulty,
            time_limit=30,
            is_active=True
        )
        db.add(question)
        db.flush()  # Get the question ID

        # Create options (correct + wrong answers)
        all_options = [q_data["correct"]] + q_data["wrong"]
        # Shuffle to randomize position
        positions = list(range(4))
        random.shuffle(positions)

        for idx, option_text in enumerate(all_options):
            option = QuestionOption(
                question_id=question.id,
                option_text=option_text,
                is_correct=(option_text == q_data["correct"]),
                option_order=positions[idx] + 1
            )
            db.add(option)

        existing_questions.add(q_data["text"])
        added_count += 1

    return added_count, skipped_count

def seed_questions(difficulty=None, check_only=False):
    """Seed questions from organized data files."""
    db = SessionLocal()

    # Check current count
    current_count = db.query(Question).count()
    print(f"\n{'='*60}")
    print("QUESTION SEEDING")
    print(f"{'='*60}")
    print(f"Current question count in database: {current_count}\n")

    if check_only:
        print("CHECK-ONLY MODE: No questions will be added\n")

    # Determine which questions to add
    if difficulty:
        questions_to_add = {difficulty: get_questions_by_difficulty(difficulty)}
    else:
        questions_to_add = get_all_questions()

    total_added = 0
    total_skipped = 0

    # Process each difficulty level
    for diff, questions in questions_to_add.items():
        if not questions:
            continue

        print(f"Processing {diff.upper()} questions...")
        added, skipped = add_questions_to_db(questions, diff, db, check_only)
        total_added += added
        total_skipped += skipped
        print(f"  {'Would add' if check_only else 'Added'}: {added}")
        print(f"  Skipped (duplicates): {skipped}\n")

    # Commit changes if not in check-only mode
    if not check_only and total_added > 0:
        db.commit()
        print("✓ Changes committed to database")

    # Final summary
    final_count = db.query(Question).count()
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    print(f"{'Would be added' if check_only else 'Added'}: {total_added} questions")
    print(f"Skipped (duplicates): {total_skipped} questions")
    print(f"Final database count: {final_count if not check_only else f'{current_count} (check-only mode)'}")
    print(f"{'='*60}\n")

    db.close()

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Seed trivia questions into the database',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        '--difficulty',
        choices=['easy', 'medium', 'hard', 'expert'],
        help='Only add questions of a specific difficulty'
    )
    parser.add_argument(
        '--check-only',
        action='store_true',
        help='Check what would be added without actually adding questions'
    )

    args = parser.parse_args()

    try:
        seed_questions(difficulty=args.difficulty, check_only=args.check_only)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
