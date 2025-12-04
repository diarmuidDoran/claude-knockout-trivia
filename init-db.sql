-- Knockout Trivia Database Initialization
-- This script creates the basic database schema.
-- Questions are seeded using Python scripts in the backend/ directory.

-- Create tables (schema only)
-- The tables will be created automatically by SQLAlchemy when the backend starts

-- Note: To populate the database with questions, use:
--   cd backend && python seed_questions.py

-- The database uses SQLAlchemy ORM which will create:
--   - rooms table
--   - players table
--   - questions table
--   - question_options table
--   - answers table
--   - player_sessions table
--   - high_scores table

-- These tables are defined in backend/app/models/models.py
-- and will be created automatically on first run.

-- Migration: Add is_ghost column to high_scores table if it doesn't exist
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_name = 'high_scores' AND column_name = 'is_ghost'
    ) THEN
        ALTER TABLE high_scores ADD COLUMN is_ghost BOOLEAN DEFAULT FALSE;
    END IF;
END $$;
