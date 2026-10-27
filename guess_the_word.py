# Mia Soard
# CIS256 Fall 2026
# Programming Assignment 4

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

# Run one round of the game
def play_game(word=None):
    if word is None:
        word = choose_word()

    # Letters guessed so far
    guessed_letters = set()
    # Incorrect guesses left
    attempts_left = MAX_ATTEMPTS

    print("**~~ Word Guessing Game ~~**")

    # Keep playing until word is solved or attempts run out
    while attempts_left > 0 and not is_word_guessed(word, guessed_letters):
        print("\nWord:", display_word(word, guessed_letters))
        print("Attempts left:", attempts_left)
        print("Guessed so far:", " ".join(sorted(guessed_letters)) or "none")

        result = process_guess(word, guessed_letters, input("Guess a letter: "))

        if result == "invalid":
            print("Please enter a single letter.")
        elif result == "repeat":
            print("Letter was already guessed.")
        elif result == "correct":
            print("Good guess!")
        else: 
            attempts_left -= 1
            print("Sorry, that letter was not in the word.")

    # Show the outcome
    if is_word_guessed(word, guessed_letters):
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"\nSorry, out of attempts! The word was: {word}")

if __name__ == "__main__":
    play_game()