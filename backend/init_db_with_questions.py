#!/usr/bin/env python3
"""
Initialize database with all tables and seed with questions.
This script combines table creation and question seeding.
"""

import sys
sys.path.insert(0, '.')

from app.models.database import engine, Base
from app.models.models import Room, Player, Question, QuestionOption, Answer

def init_database():
    """Create all database tables."""
    print("="*60)
    print("DATABASE INITIALIZATION")
    print("="*60)
    print()

    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("✓ Database tables created successfully!")
    print("\nTables created:")
    print("  - rooms")
    print("  - players")
    print("  - questions")
    print("  - question_options")
    print("  - answers")
    print("  - player_sessions")
    print()

    # Check if questions already exist
    from app.models.database import SessionLocal
    db = SessionLocal()
    question_count = db.query(Question).count()
    db.close()

    if question_count > 0:
        print(f"✓ Database already contains {question_count} questions")
        print("  To reseed questions, use: python seed_questions.py")
    else:
        print("⚠  Database is empty")
        print("  To add questions, run: python seed_questions.py")

    print()
    print("="*60)
    print("✅ DATABASE INITIALIZATION COMPLETE")
    print("="*60)
    print()

if __name__ == "__main__":
    init_database()
