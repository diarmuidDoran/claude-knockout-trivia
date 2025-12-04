#!/usr/bin/env python3
"""
Update database schema with new tables.
Run this when you add new models to update the database schema.
"""
import sys
sys.path.insert(0, '.')

from app.models.database import engine, Base
from app.models.models import PlayerSession

def update_database():
    print("Updating database schema...")
    # Create all tables (will only create new ones that don't exist)
    Base.metadata.create_all(bind=engine)
    print("✓ Database schema updated successfully!")

if __name__ == "__main__":
    update_database()
