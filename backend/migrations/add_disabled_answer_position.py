"""
Migration: Add disabled_answer_position field to players table

This field stores which answer position (1-4) is disabled for a player
after they participate in the "Playing at a Disadvantage" mini-game.

The disabled position persists for all remaining trivia questions.

Run this script to add the field to existing databases:
    python backend/migrations/add_disabled_answer_position.py
"""

import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine, text
from app.models.database import DATABASE_URL

def run_migration():
    """Add disabled_answer_position column to players table"""
    engine = create_engine(DATABASE_URL)

    with engine.connect() as connection:
        # Start transaction
        trans = connection.begin()

        try:
            print("Adding disabled_answer_position column to players table...")

            # Add column
            connection.execute(text(
                """
                ALTER TABLE players
                ADD COLUMN disabled_answer_position INTEGER NULL
                """
            ))

            print("✓ Column added successfully")
            print("  - Field: disabled_answer_position")
            print("  - Type: INTEGER")
            print("  - Nullable: Yes")
            print("  - Purpose: Stores disabled answer position (1-4) from Playing at a Disadvantage mini-game")

            # Commit transaction
            trans.commit()
            print("\n✓ Migration completed successfully!")

        except Exception as e:
            # Rollback on error
            trans.rollback()
            print(f"\n✗ Migration failed: {str(e)}")
            raise

if __name__ == "__main__":
    print("=" * 60)
    print("MIGRATION: Add disabled_answer_position to players")
    print("=" * 60)
    print()

    try:
        run_migration()
    except Exception as e:
        print(f"\nError: {str(e)}")
        sys.exit(1)
