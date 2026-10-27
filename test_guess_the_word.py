# pytest tests for guess_the_word.py

from guess_the_word import (
    WORDS,
    choose_word,
    display_word,
    process_guess,
    is_word_guessed,
)

# Word selection

def test_chosen_word_is_in_list():
    # Run many times since the choice is random
    for _ in range(50):
        assert choose_word() in WORDS

def test_choose_word_from_custom_list():
    assert choose_word(["beauty"]) == "beauty"

# Process guesses

def test_correct_guess():
    guessed = set()
    assert process_guess("bestie", guessed, "b") == "correct"
    assert "b" in guessed

def test_incorrect_guess():
    guessed = set()
    assert process_guess("bestie", guessed, "l") == "incorrect"
    assert "l" in guessed

def test_repeated_guess():
    guessed = {"b"}
    assert process_guess("bestie", guessed, "b") == "repeat"

def test_invalid_guesses():
    guessed = set()
    assert process_guess("bestie", guessed, "") == "invalid"
    assert process_guess("bestie", guessed, "ab") == "invalid"
    assert process_guess("bestie", guessed, "5") == "invalid"
    assert guessed == set()

def test_if_guess_is_case_insensitive():
    guessed = set()
    assert process_guess("bestie", guessed, "B") == "correct"
    assert "b" in guessed


# Display and win condition

def test_hides_unguessed_letters():
    assert display_word("cat", {"c"}) == "c _ _"

def test_letters_can_be_guessed_in_any_order():
    assert display_word("cat", {"t", "c"}) == "c _ t"

def test_word_guessed_detection():
    assert not is_word_guessed("cat", {"c", "a"})
    assert is_word_guessed("cat", {"c", "a", "t"})

def test_reveals_all_instances_of_letter():
    # 'e' appears twice in "bestie"; both should be revealed at once
    assert display_word("bestie", {"e"}) == "_ e _ _ _ e"