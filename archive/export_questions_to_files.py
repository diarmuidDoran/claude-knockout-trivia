#!/usr/bin/env python3
"""
Export all questions from the database and populate the difficulty-based data files.
This script extracts questions from the running database and organizes them into the
questions_data directory structure.
"""

import sys
sys.path.insert(0, '.')

def fetch_all_questions():
    """Fetch all questions through the API."""
    try:
        # Since there's no direct export endpoint, we'll use database connection
        from app.models.database import SessionLocal
        from app.models.models import Question, QuestionOption

        db = SessionLocal()

        all_questions = db.query(Question).all()

        questions_by_difficulty = {
            'easy': [],
            'medium': [],
            'hard': [],
            'expert': []
        }

        for question in all_questions:
            # Get options for this question
            options = db.query(QuestionOption).filter(
                QuestionOption.question_id == question.id
            ).order_by(QuestionOption.option_order).all()

            correct_answer = None
            wrong_answers = []

            for option in options:
                if option.is_correct:
                    correct_answer = option.option_text
                else:
                    wrong_answers.append(option.option_text)

            # Create question dict
            q_dict = {
                "text": question.question_text,
                "category": question.category,
                "correct": correct_answer,
                "wrong": wrong_answers
            }

            # Add to appropriate difficulty list
            difficulty = question.difficulty.lower()
            if difficulty in questions_by_difficulty:
                questions_by_difficulty[difficulty].append(q_dict)

        db.close()
        return questions_by_difficulty

    except Exception as e:
        print(f"Error fetching questions: {e}")
        return None

def format_question_for_python(q):
    """Format a question dict as Python code."""
    return f"""    {{
        "text": {repr(q['text'])},
        "category": {repr(q['category'])},
        "correct": {repr(q['correct'])},
        "wrong": {repr(q['wrong'])}
    }}"""

def write_difficulty_file(difficulty, questions):
    """Write questions to a difficulty file."""
    filename = f'questions_data/{difficulty}_questions.py'

    # Header based on difficulty
    headers = {
        'easy': f'''"""Easy difficulty trivia questions.

This module contains easy difficulty questions for the trivia game.
Total: {len(questions)} questions

Add new easy questions here in the following format:
{{
    "text": "What is the question?",
    "category": "Category Name",
    "correct": "Correct Answer",
    "wrong": ["Wrong Answer 1", "Wrong Answer 2", "Wrong Answer 3"]
}}
"""''',
        'medium': f'''"""Medium difficulty trivia questions.

This module contains medium difficulty questions for the trivia game.
Total: {len(questions)} questions

Add new medium questions here in the following format:
{{
    "text": "What is the question?",
    "category": "Category Name",
    "correct": "Correct Answer",
    "wrong": ["Wrong Answer 1", "Wrong Answer 2", "Wrong Answer 3"]
}}
"""''',
        'hard': f'''"""Hard difficulty trivia questions.

This module contains hard difficulty questions for the trivia game.
Total: {len(questions)} questions

Add new hard questions here in the following format:
{{
    "text": "What is the question?",
    "category": "Category Name",
    "correct": "Correct Answer",
    "wrong": ["Wrong Answer 1", "Wrong Answer 2", "Wrong Answer 3"]
}}
"""''',
        'expert': f'''"""Expert difficulty trivia questions.

This module contains expert difficulty questions for the trivia game.
Total: {len(questions)} questions

Add new expert questions here in the following format:
{{
    "text": "What is the question?",
    "category": "Category Name",
    "correct": "Correct Answer",
    "wrong": ["Wrong Answer 1", "Wrong Answer 2", "Wrong Answer 3"]
}}
"""'''
    }

    with open(filename, 'w') as f:
        f.write(headers[difficulty])
        f.write('\n\n')
        f.write(f'{difficulty.upper()}_QUESTIONS = [\n')

        for i, q in enumerate(questions):
            f.write(format_question_for_python(q))
            if i < len(questions) - 1:
                f.write(',\n')
            else:
                f.write('\n')

        f.write(']\n')

    print(f"✓ Wrote {len(questions)} questions to {filename}")

def main():
    """Main function."""
    print("="*60)
    print("EXPORTING QUESTIONS FROM DATABASE")
    print("="*60)
    print()

    # Fetch all questions
    print("Fetching questions from database...")
    questions_by_difficulty = fetch_all_questions()

    if not questions_by_difficulty:
        print("❌ Failed to fetch questions")
        sys.exit(1)

    # Summary
    print()
    print("Questions by difficulty:")
    total = 0
    for diff, questions in sorted(questions_by_difficulty.items()):
        count = len(questions)
        total += count
        print(f"  {diff.capitalize():10s}: {count:4d} questions")
    print(f"  {'Total':10s}: {total:4d} questions")
    print()

    # Write to files
    print("Writing to difficulty files...")
    for difficulty, questions in questions_by_difficulty.items():
        write_difficulty_file(difficulty, questions)

    print()
    print("="*60)
    print("✅ EXPORT COMPLETE")
    print("="*60)
    print()
    print("Questions have been exported to questions_data/ directory:")
    print("  - easy_questions.py")
    print("  - medium_questions.py")
    print("  - hard_questions.py")
    print("  - expert_questions.py")
    print()

if __name__ == "__main__":
    main()
