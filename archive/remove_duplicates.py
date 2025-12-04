#!/usr/bin/env python3
"""Remove duplicate questions from the database."""

import sys
sys.path.insert(0, '.')

from app.models.database import SessionLocal
from app.models.models import Question, QuestionOption, Answer
from collections import defaultdict

def remove_duplicates():
    """Remove duplicate questions, keeping the first occurrence."""
    db = SessionLocal()

    # Get all questions
    all_questions = db.query(Question).all()
    print(f'Total questions before cleanup: {len(all_questions)}')

    # Group questions by text
    questions_by_text = defaultdict(list)
    for q in all_questions:
        questions_by_text[q.question_text].append(q)

    # Find and remove duplicates
    duplicates_removed = 0
    for text, questions in questions_by_text.items():
        if len(questions) > 1:
            print(f'\nFound {len(questions)} instances of: {text[:60]}...')
            # Keep the first one, delete the rest
            to_delete = questions[1:]
            for q in to_delete:
                print(f'  Deleting question ID {q.id}')

                # Delete associated answers first (if any)
                db.query(Answer).filter(Answer.question_id == q.id).delete()

                # Delete associated options
                db.query(QuestionOption).filter(QuestionOption.question_id == q.id).delete()

                # Delete the question
                db.delete(q)
                duplicates_removed += 1

    db.commit()

    # Verify final count
    final_count = db.query(Question).count()
    print(f'\n{"="*60}')
    print(f'✓ Removed {duplicates_removed} duplicate questions')
    print(f'✓ Total unique questions: {final_count}')
    print(f'{"="*60}')

    # Show distribution
    from collections import Counter
    questions = db.query(Question).all()
    categories = Counter([q.category for q in questions])
    difficulties = Counter([q.difficulty for q in questions])

    print(f'\n📊 QUESTIONS BY CATEGORY:')
    for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
        print(f'  {cat:20s}: {count:3d}')

    print(f'\n📈 QUESTIONS BY DIFFICULTY:')
    for diff, count in sorted(difficulties.items()):
        print(f'  {diff:20s}: {count:3d}')

    print(f'\n{"="*60}')
    print('✅ Database cleanup complete!')
    print('   All questions are unique and ready for random selection')
    print(f'{"="*60}\n')

    db.close()

if __name__ == "__main__":
    remove_duplicates()
