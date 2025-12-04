from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text, Float, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from .database import Base

class GameState(enum.Enum):
    WAITING = "waiting"
    STARTING = "starting"
    ACTIVE = "active"
    FINISHED = "finished"

class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(6), unique=True, index=True, nullable=False)
    host_name = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    max_players = Column(Integer, default=10)
    current_question_id = Column(Integer, ForeignKey("questions.id"), nullable=True)
    game_state = Column(Enum(GameState), default=GameState.WAITING)
    question_start_time = Column(DateTime, nullable=True)
    is_haunting_race_active = Column(Boolean, default=False)

    # Relationships
    players = relationship("Player", back_populates="room", cascade="all, delete-orphan")
    current_question = relationship("Question", foreign_keys=[current_question_id])

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    room_id = Column(Integer, ForeignKey("rooms.id"))
    joined_at = Column(DateTime, default=datetime.utcnow)
    is_connected = Column(Boolean, default=True)
    is_vip = Column(Boolean, default=False)
    total_score = Column(Integer, default=0)
    is_ghost = Column(Boolean, default=False)  # True if eliminated but still playing
    eliminated_at = Column(DateTime, nullable=True)  # When player was eliminated
    disabled_answer_position = Column(Integer, nullable=True)  # Answer position disabled (1-4) from Playing at a Disadvantage

    # Relationships
    room = relationship("Room", back_populates="players")
    answers = relationship("Answer", back_populates="player", cascade="all, delete-orphan")

class Question(Base):
    __tablename__ = "questions"
    
    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(Text, nullable=False)
    category = Column(String(50), nullable=False)  # general, current_events, pop_culture
    difficulty = Column(String(20), default="medium")  # easy, medium, hard
    time_limit = Column(Integer, default=30)  # seconds
    created_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    
    # Relationships
    options = relationship("QuestionOption", back_populates="question", cascade="all, delete-orphan")
    answers = relationship("Answer", back_populates="question", cascade="all, delete-orphan")

class QuestionOption(Base):
    __tablename__ = "question_options"
    
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.id"))
    option_text = Column(Text, nullable=False)
    is_correct = Column(Boolean, default=False)
    option_order = Column(Integer, nullable=False)  # A=1, B=2, C=3, D=4
    
    # Relationships
    question = relationship("Question", back_populates="options")

class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("players.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    selected_option_id = Column(Integer, ForeignKey("question_options.id"))
    answered_at = Column(DateTime, default=datetime.utcnow)
    response_time = Column(Float)  # seconds from question start
    points_earned = Column(Integer, default=0)

    # Relationships
    player = relationship("Player", back_populates="answers")
    question = relationship("Question", back_populates="answers")
    selected_option = relationship("QuestionOption")

class HighScore(Base):
    __tablename__ = "high_scores"

    id = Column(Integer, primary_key=True, index=True)
    player_name = Column(String(50), nullable=False)
    score = Column(Integer, nullable=False)
    questions_answered = Column(Integer, default=0)
    correct_answers = Column(Integer, default=0)
    achieved_at = Column(DateTime, default=datetime.utcnow)
    room_code = Column(String(6), nullable=True)  # For reference, not a FK since rooms get deleted
    is_ghost = Column(Boolean, default=False)  # Track if they were a ghost player

class PlayerSession(Base):
    __tablename__ = "player_sessions"

    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("players.id"), nullable=False)
    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=False)
    session_token = Column(String(64), unique=True, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, nullable=False)

    # Relationships
    player = relationship("Player")
    room = relationship("Room")

class HauntingRaceQuestion(Base):
    __tablename__ = "haunting_race_questions"

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(Text, nullable=False)  # Context/topic for the statements
    category = Column(String(50), nullable=False)  # history, science, geography, etc.
    difficulty = Column(String(20), default="medium")  # easy, medium, hard
    time_limit = Column(Integer, default=40)  # seconds - longer than regular trivia
    created_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)

    # Relationships
    statements = relationship("HauntingRaceStatement", back_populates="question", cascade="all, delete-orphan")

class HauntingRaceStatement(Base):
    __tablename__ = "haunting_race_statements"

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("haunting_race_questions.id"))
    statement_text = Column(Text, nullable=False)
    is_true = Column(Boolean, nullable=False)  # True or False
    statement_order = Column(Integer, nullable=False)  # 1, 2, or 3
    is_ghost_only = Column(Boolean, default=False)  # If True, only ghosts see this (3rd option)

    # Relationships
    question = relationship("HauntingRaceQuestion", back_populates="statements")