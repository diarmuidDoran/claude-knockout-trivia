# Archived Files

This directory contains old question generation files that have been replaced by the new organized system.

## Archived SQL Files

### init-db.sql (Old)
- Original database initialization script with ~200 hardcoded questions
- Replaced by: SQLAlchemy automatic table creation + backend/seed_questions.py

### trivia-questions-200.sql
- SQL file with 200 trivia questions
- Replaced by: backend/questions_data/ directory structure

### trivia-questions-complete.sql
- Complete SQL export of questions
- Replaced by: backend/questions_data/ directory structure

## Why Were These Archived?

The project has migrated to a better system:

**Old System** (Archived):
- SQL files with hardcoded questions
- Mixed Python generation scripts in root directory
- Difficult to maintain and update

**New System** (Current):
- Organized Python data files in `backend/questions_data/`
- Questions grouped by difficulty (easy, medium, hard, expert)
- Unified seeding script: `backend/seed_questions.py`
- All 1,000 questions properly organized and documented

## Archived Backend Scripts

### export_questions_to_files.py
- **Purpose**: One-time migration script to export questions from database to Python files
- **Function**: Exported 1,000 questions to `backend/questions_data/` directory
- **Archived**: 2025-11-30 (migration complete, files generated)

### remove_duplicates.py
- **Purpose**: One-time cleanup to remove duplicate questions from database
- **Function**: Kept first occurrence of each question, deleted duplicates
- **Archived**: 2025-11-30 (cleanup complete, no longer needed)

### setup_haunting_race_db.py
- **Purpose**: One-time setup to create haunting race database tables
- **Function**: Created `haunting_race_questions` and `haunting_race_statements` tables
- **Archived**: 2025-11-30 (functionality now integrated into `backend/init_db.py` and `backend/recreate_db.py`)

## Restoring Old Files

If you need to reference these old files:
1. They are preserved in this `archive/` directory
2. The database currently contains 1,000 questions exported from the old system
3. Archived scripts can still be run if needed (though not recommended)

## Migration History

### 2025-11-18 - Question System Migration
- ✅ All 1,000 questions exported from database
- ✅ Questions organized into difficulty-based files
- ✅ Old generation scripts removed from root
- ✅ New unified seeding system in place

### 2025-11-30 - Backend Cleanup
- ✅ Moved one-time migration scripts to archive
- ✅ Archived redundant setup scripts
- ✅ Backend now contains only core utilities and active tools
- ✅ Updated .gitignore for better OS file exclusion
