# Word guessing game.
# Guess the word one letter at a time

import random

# List of words the game will choose from
WORDS = ["sunshine", "lollipop", "rainbow", "sparkle", "kitten", "bubbly", "bestie"]

# Number of incorrect guesses allowed before player loses
MAX_ATTEMPTS = 8

# Return a random word from the list
def choose_word(words=WORDS):
    return random.choice(words)

