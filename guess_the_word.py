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

# Return the word with unguessed letters hidden, e.g. "s_ns_ine"
def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

# Process one guess and update guessed_letters in place
def process_guess(word, guessed_letters, guess):
    guess = guess.lower().strip()

    # Only accept one letter
    if len(guess) != 1 or not guess.isalpha():
        return "invalid"

    # No penalty for repeated guesses
    if guess in guessed_letters:
        return "repeat"

    guessed_letters.add(guess)
    return "correct" if guess in word else "incorrect"

# Return true if every letter in the word is guessed
def is_word_guessed(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)

