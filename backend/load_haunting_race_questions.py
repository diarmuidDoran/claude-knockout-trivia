#!/usr/bin/env python3
"""
Load haunting race questions from JSON file into database.

Usage:
    python3 load_haunting_race_questions.py
"""

import sys
import json
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from app.models.database import SessionLocal
from app.models.models import HauntingRaceQuestion, HauntingRaceStatement

def load_questions():
    """Load questions from JSON file into database."""
    print("=" * 60)
    print("Loading Haunting Race Questions")
    print("=" * 60)

    # Path to JSON file
    json_file = Path(__file__).parent / "haunting_race_questions.json"

    if not json_file.exists():
        print(f"\n✗ Error: Question file not found at {json_file}")
        sys.exit(1)

    print(f"\n[1/4] Reading questions from {json_file.name}...")

    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        questions = data.get('questions', [])
        print(f"✓ Found {len(questions)} questions")

    except Exception as e:
        print(f"✗ Error reading JSON file: {e}")
        sys.exit(1)

    # Connect to database
    print("\n[2/4] Connecting to database...")
    db = SessionLocal()

    try:
        # Check if questions already exist
        existing_count = db.query(HauntingRaceQuestion).count()
        if existing_count > 0:
            print(f"\n⚠ Warning: {existing_count} questions already exist in database")

            # Check if running in non-interactive environment (like Railway)
            import sys
            if not sys.stdin.isatty():
                print("Non-interactive environment detected. Skipping duplicate questions.")
                print("Questions already loaded. Exiting.")
                return

            # Interactive environment - ask user
            response = input("Do you want to delete existing questions and reload? (y/N): ")
            if response.lower() == 'y':
                print("Deleting existing questions...")
                db.query(HauntingRaceStatement).delete()
                db.query(HauntingRaceQuestion).delete()
                db.commit()
                print("✓ Existing questions deleted")
            else:
                print("Skipping load. Exiting.")
                return

        # Load questions
        print(f"\n[3/4] Loading {len(questions)} questions into database...")
        loaded_count = 0
        error_count = 0

        for idx, q_data in enumerate(questions, 1):
            try:
                # Create question
                question = HauntingRaceQuestion(
                    question_text=q_data['question_text'],
                    category=q_data['category'],
                    difficulty=q_data.get('difficulty', 'medium'),
                    time_limit=40,
                    is_active=True
                )
                db.add(question)
                db.flush()  # Get the question ID

                # Create statements
                for stmt_data in q_data['statements']:
                    statement = HauntingRaceStatement(
                        question_id=question.id,
                        statement_text=stmt_data['text'],
                        is_true=stmt_data['is_true'],
                        statement_order=stmt_data['order'],
                        is_ghost_only=stmt_data.get('ghost_only', False)
                    )
                    db.add(statement)

                loaded_count += 1

                # Show progress every 50 questions
                if idx % 50 == 0:
                    print(f"  Progress: {idx}/{len(questions)} questions loaded...")

            except Exception as e:
                error_count += 1
                print(f"  ✗ Error loading question {idx}: {e}")
                continue

        # Commit all changes
        db.commit()

        print(f"\n[4/4] Load complete!")
        print(f"  ✓ Successfully loaded: {loaded_count} questions")
        if error_count > 0:
            print(f"  ✗ Errors: {error_count} questions")

        # Verify counts
        print("\n" + "=" * 60)
        print("Database Statistics")
        print("=" * 60)
        final_question_count = db.query(HauntingRaceQuestion).count()
        final_statement_count = db.query(HauntingRaceStatement).count()
        print(f"Total questions: {final_question_count}")
        print(f"Total statements: {final_statement_count}")

        # Show category breakdown
        print("\nQuestions by category:")
        from sqlalchemy import func
        category_counts = db.query(
            HauntingRaceQuestion.category,
            func.count(HauntingRaceQuestion.id)
        ).group_by(HauntingRaceQuestion.category).all()

        for category, count in sorted(category_counts, key=lambda x: x[1], reverse=True):
            print(f"  {category}: {count}")

        print("\n" + "=" * 60)
        print("✓ Questions loaded successfully!")
        print("=" * 60)
        print("\nThe haunting race feature is now ready to use!")

    except Exception as e:
        print(f"\n✗ Error loading questions: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
        sys.exit(1)
    finally:
        db.close()

if __name__ == "__main__":
    load_questions()
