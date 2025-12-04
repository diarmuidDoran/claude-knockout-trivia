"""
Opinion Questions for Worst Answer Mini-Game

These are fun, open-ended questions where players submit what they think
is the worst (or best) answer. Questions should be:
- Fun and light-hearted
- Not offensive or controversial
- Easy to understand
- Allow for creative/funny answers
- Safe for all audiences

Format: Questions can ask for the "worst" or "best" of something.
Players will submit what they think is the worst/best answer.
"""

OPINION_QUESTIONS = [
    # Entertainment & Pop Culture
    "What is the worst song to sing for karaoke?",
    "What is the worst movie to watch on a date?",
    "What is the best TV show ever made?",
    "What is the worst pickup line?",
    "What is the best video game of all time?",
    "What is the worst Halloween costume?",
    "What is the best superhero power to have?",
    "What is the worst thing to say in a movie theater?",

    # Food & Drink
    "What is the best food as a last meal?",
    "What is the best pizza topping?",
    "What is the best ice cream flavor?",
    "What is the best breakfast food?",
    "What is the worst thing to find in your food?",
    "What is the best candy?",
    "What is the best way to eat an Oreo?",
    "What is the worst food to eat on a first date?",

    # Social Situations
    "What is the worst gift to give someone?",
    "What is the worst place to go on a first date?",
    "What is the worst excuse for being late?",
    "What is the worst thing to say in a job interview?",
    "What is the worst name for a baby?",
    "What is the best way to spend a weekend?",
    "What is the worst conversation topic at dinner?",
    "What is the best way to make a first impression?",

    # Daily Life & Random
    "What is the best animal to have as a pet?",
    "What is the worst thing to forget on vacation?",
    "What is the worst thing to step on barefoot?",
    "What is the best thing to do when bored?",
    "What is the worst smell?",
    "What is the worst sound to wake up to?",
    "What is the best board game?",
    "What is the best season of the year?",
    "What is the worst fashion trend?",
    "What is the best thing about being an adult?",
    "What is the worst day of the week?",
    "What is the best way to relax?",

    # Additional Questions
    "What is the worst time to receive a phone call?",
    "What is the best type of weather?",
    "What is the worst thing to lose?",
    "What is the best hobby to have?",
    "What is the worst place to get stuck?",
    "What is the best dessert?",
    "What is the worst chore to do?",
    "What is the best way to travel?",
    "What is the worst thing to run out of?",
    "What is the best room in a house?",
    "What is the worst thing to wear to a wedding?",
    "What is the best sport to watch?",
    "What is the worst thing to forget at home?",
    "What is the best holiday?",
    "What is the worst thing to break?",
    "What is the best type of music?",
    "What is the worst thing to spill?",
    "What is the best way to exercise?",
]

def get_random_question() -> str:
    """
    Get a random opinion question.

    Returns:
        A random opinion question string
    """
    import random
    return random.choice(OPINION_QUESTIONS)

def get_all_questions() -> list:
    """
    Get all opinion questions.

    Returns:
        List of all opinion question strings
    """
    return OPINION_QUESTIONS.copy()

def add_custom_question(question: str) -> bool:
    """
    Add a custom opinion question to the list.

    Args:
        question: The question to add

    Returns:
        True if added successfully, False if invalid
    """
    if not question or len(question) > 100:
        return False

    if question not in OPINION_QUESTIONS:
        OPINION_QUESTIONS.append(question)
        return True

    return False

# Total count for reference
TOTAL_QUESTIONS = len(OPINION_QUESTIONS)
