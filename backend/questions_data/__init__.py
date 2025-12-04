"""Question data organized by difficulty level."""

from .easy_questions import EASY_QUESTIONS
from .medium_questions import MEDIUM_QUESTIONS
from .hard_questions import HARD_QUESTIONS
from .expert_questions import EXPERT_QUESTIONS

__all__ = ['EASY_QUESTIONS', 'MEDIUM_QUESTIONS', 'HARD_QUESTIONS', 'EXPERT_QUESTIONS']

def get_all_questions():
    """Get all questions from all difficulty levels."""
    return {
        'easy': EASY_QUESTIONS,
        'medium': MEDIUM_QUESTIONS,
        'hard': HARD_QUESTIONS,
        'expert': EXPERT_QUESTIONS
    }

def get_questions_by_difficulty(difficulty):
    """Get questions for a specific difficulty level."""
    questions_map = {
        'easy': EASY_QUESTIONS,
        'medium': MEDIUM_QUESTIONS,
        'hard': HARD_QUESTIONS,
        'expert': EXPERT_QUESTIONS
    }
    return questions_map.get(difficulty, [])
