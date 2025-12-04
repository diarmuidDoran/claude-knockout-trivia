#!/bin/bash
# PostgreSQL Database Setup Script for Knockout Trivia

echo "🗄️  Knockout Trivia - PostgreSQL Setup"
echo "======================================"
echo ""

# Check if PostgreSQL is installed
if ! command -v psql &> /dev/null; then
    echo "❌ PostgreSQL is not installed!"
    echo ""
    echo "📦 Install PostgreSQL:"
    echo ""
    echo "On macOS (with Homebrew):"
    echo "  brew install postgresql@15"
    echo "  brew services start postgresql@15"
    echo ""
    echo "On Ubuntu/Debian:"
    echo "  sudo apt-get update"
    echo "  sudo apt-get install postgresql postgresql-contrib"
    echo "  sudo systemctl start postgresql"
    echo ""
    exit 1
fi

echo "✓ PostgreSQL is installed"
echo ""

# Database configuration
DB_NAME="knockout_trivia"
DB_USER="postgres"
DB_PASS="password"

echo "📋 Database Configuration:"
echo "  Database: $DB_NAME"
echo "  User: $DB_USER"
echo "  Password: $DB_PASS"
echo ""

# Create database
echo "🔨 Creating database '$DB_NAME'..."
createdb -U $DB_USER $DB_NAME 2>/dev/null

if [ $? -eq 0 ]; then
    echo "✓ Database created successfully"
else
    echo "⚠️  Database may already exist (this is okay)"
fi

echo ""
echo "✅ PostgreSQL setup complete!"
echo ""
echo "📝 Next steps:"
echo "  1. Update backend/.env with your PostgreSQL credentials if different"
echo "  2. Run: python3 recreate_db.py"
echo "  3. Start the backend: python3 -m uvicorn app.main:app --reload --port 8001 --host 0.0.0.0"
echo ""
