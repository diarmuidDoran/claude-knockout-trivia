#!/bin/bash
set -e

echo "🚀 Knockout Trivia Backend - Docker Startup"
echo "=========================================="

# Wait for PostgreSQL to be ready
echo ""
echo "⏳ Waiting for PostgreSQL to be ready..."
until pg_isready -h postgres -p 5432 -U postgres; do
  echo "   PostgreSQL is unavailable - sleeping"
  sleep 2
done
echo "✓ PostgreSQL is ready!"

# Check if database is initialized
echo ""
echo "🔍 Checking database initialization..."
TABLES_EXIST=$(python3 -c "
import sys
from app.models.database import engine
from sqlalchemy import inspect
inspector = inspect(engine)
tables = inspector.get_table_names()
sys.exit(0 if len(tables) > 0 else 1)
" 2>/dev/null && echo "yes" || echo "no")

if [ "$TABLES_EXIST" = "no" ]; then
    echo "📋 Database is empty. Initializing..."

    # Create database schema
    echo ""
    echo "   [1/4] Creating database schema..."
    python3 recreate_db.py

    # Load regular trivia questions
    echo ""
    echo "   [2/4] Loading regular trivia questions..."
    python3 seed_questions.py

    # Check if questions JSON exists, if not generate it
    if [ ! -f "haunting_race_questions.json" ]; then
        echo ""
        echo "   [3/4] Generating haunting race questions..."
        python3 generate_haunting_questions.py
    else
        echo ""
        echo "   [3/4] Using existing haunting race questions..."
    fi

    # Load haunting race questions into database
    echo ""
    echo "   [4/4] Loading haunting race questions..."
    python3 load_haunting_race_questions.py <<EOF
y
EOF

    echo ""
    echo "✅ Database initialization complete!"
else
    echo "✓ Database already initialized"
fi

# Start the FastAPI application
echo ""
echo "🎮 Starting Knockout Trivia API..."
echo "=========================================="
echo ""

exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
