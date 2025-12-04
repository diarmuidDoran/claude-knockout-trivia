import os
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey, Text, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/knockout_trivia")

# Railway compatibility: convert postgres:// to postgresql://
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Log connection info (hide password for security)
db_host = DATABASE_URL.split('@')[1].split('/')[0] if '@' in DATABASE_URL else 'localhost'
print(f"[INFO] Connecting to database at: {db_host}")

# Warn if using default localhost database (likely misconfiguration in production)
if 'localhost' in DATABASE_URL and os.getenv("RAILWAY_ENVIRONMENT"):
    print("[WARNING] Using localhost database in Railway! DATABASE_URL may not be set correctly.")
    print("[WARNING] Make sure PostgreSQL service is added and variables are shared.")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()