#!/usr/bin/env python3
"""Initialize the database and create all tables."""

import sys
sys.path.insert(0, '.')

from app.models.database import engine, Base
from app.models.models import Room, Player, Question, QuestionOption, Answer

def init_database():
    """Create all database tables."""
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("✓ Database tables created successfully!")
    print("\nTables created:")
    print("  - rooms")
    print("  - players")
    print("  - questions")
    print("  - question_options")
    print("  - answers")

if __name__ == "__main__":
    init_database()
