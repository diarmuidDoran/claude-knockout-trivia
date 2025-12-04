#!/usr/bin/env python3
"""
Database setup script for Haunting Race tables.
Run this script to create the haunting_race_questions and haunting_race_statements tables.

Usage:
    python3 setup_haunting_race_db.py
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from app.models.database import engine, Base
from app.models.models import HauntingRaceQuestion, HauntingRaceStatement

def setup_tables():
    """Create haunting race tables if they don't exist."""
    print("=" * 60)
    print("Setting up Haunting Race Database Tables")
    print("=" * 60)

    try:
        # Create tables
        print("\n[1/2] Creating tables...")
        Base.metadata.create_all(bind=engine)
        print("✓ Tables created successfully!")

        # Verify tables exist
        print("\n[2/2] Verifying tables...")
        from sqlalchemy import inspect
        inspector = inspect(engine)
        tables = inspector.get_table_names()

        if 'haunting_race_questions' in tables:
            print("✓ haunting_race_questions table exists")
        else:
            print("✗ haunting_race_questions table not found")

        if 'haunting_race_statements' in tables:
            print("✓ haunting_race_statements table exists")
        else:
            print("✗ haunting_race_statements table not found")

        print("\n" + "=" * 60)
        print("Database setup complete!")
        print("=" * 60)
        print("\nNext step: Run load_haunting_race_questions.py to populate questions")

    except Exception as e:
        print(f"\n✗ Error setting up database: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    setup_tables()
