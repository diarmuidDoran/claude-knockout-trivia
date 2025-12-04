#!/usr/bin/env python3
"""
Add ghost player fields to Player model.

This migration adds:
- is_ghost: Boolean field to track eliminated players
- eliminated_at: DateTime field to track when player was eliminated
"""

import sys
sys.path.insert(0, '.')

from app.models.database import engine
from sqlalchemy import text

def upgrade():
    """Add ghost player fields to players table."""
    with engine.connect() as conn:
        # Add is_ghost column
        conn.execute(text("""
            ALTER TABLE players
            ADD COLUMN IF NOT EXISTS is_ghost BOOLEAN DEFAULT FALSE
        """))

        # Add eliminated_at column
        conn.execute(text("""
            ALTER TABLE players
            ADD COLUMN IF NOT EXISTS eliminated_at TIMESTAMP
        """))

        conn.commit()

    print("✓ Added is_ghost and eliminated_at fields to players table")

def downgrade():
    """Remove ghost player fields from players table."""
    with engine.connect() as conn:
        conn.execute(text("""
            ALTER TABLE players
            DROP COLUMN IF EXISTS is_ghost
        """))

        conn.execute(text("""
            ALTER TABLE players
            DROP COLUMN IF EXISTS eliminated_at
        """))

        conn.commit()

    print("✓ Removed is_ghost and eliminated_at fields from players table")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "downgrade":
        downgrade()
    else:
        upgrade()
