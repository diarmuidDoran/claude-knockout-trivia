#!/usr/bin/env python3
"""
Script to recreate the PostgreSQL database with new schema.
This will drop all existing tables and create new ones with the updated schema.
"""
import os
from dotenv import load_dotenv
from app.models.database import engine, Base
from app.models.models import (
    Room, Player, Question, QuestionOption, Answer, PlayerSession,
    HauntingRaceQuestion, HauntingRaceStatement
)

# Load environment variables
load_dotenv()

def recreate_database():
    """Drop all existing tables and create new ones with updated schema."""

    print("🗄️  PostgreSQL Database Recreation")
    print("=" * 50)

    # Display database URL (hide password)
    db_url = os.getenv("DATABASE_URL", "Not configured")
    safe_url = db_url.replace(db_url.split('@')[0].split(':')[-1], '****') if '@' in db_url else db_url
    print(f"\nDatabase: {safe_url}")

    # Drop all existing tables
    print("\n🗑️  Dropping all existing tables...")
    try:
        Base.metadata.drop_all(bind=engine)
        print("✓ All tables dropped successfully")
    except Exception as e:
        print(f"⚠️  Warning during drop: {e}")
        print("   (This is normal if tables don't exist yet)")

    # Create all tables with new schema
    print("\n📋 Creating new database schema...")
    try:
        Base.metadata.create_all(bind=engine)
        print("✓ All tables created successfully!")
    except Exception as e:
        print(f"❌ Error creating tables: {e}")
        return False

    print("\n✅ Database recreation complete!")
    print("\n📦 Tables created:")
    print("  • rooms (with is_haunting_race_active field)")
    print("  • players")
    print("  • questions")
    print("  • question_options")
    print("  • answers")
    print("  • player_sessions")
    print("  • haunting_race_questions")
    print("  • haunting_race_statements")
    print("\n⚠️  Note: All existing game data has been cleared.")

    return True

if __name__ == "__main__":
    success = recreate_database()
    exit(0 if success else 1)
