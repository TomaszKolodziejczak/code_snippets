from string import ascii_lowercase
from typing import List
from Words import get_random_word

""" refactoring needed """

def get_users_attempt() -> int:
    """Ask user about number of incorrect attempts for the game."""
    while True:
        num_of_attempts = input("How many attempts do you want? [1-25]: ")
        try:
            num_of_attempts = int(num_of_attempts)
            if 1 <= num_of_attempts <= 25:
                return num_of_attempts
            else:
                print(f'{num_of_attempts} is not in range 1-25')
        except ValueError:
            print(f'{num_of_attempts} is not an integer in range 1-25')


def get_min_word_length() -> int:
    """Ask user about min length of word"""
    while True:
        word_length = input("How many letters should be in guess word? [4-16]: ")
        try:
            word_length = int(word_length)
            if 4 <= word_length <= 16:
                return word_length
            else:
                print(f'{word_length} is not in range 4-16')
        except ValueError:
            print(f'{word_length} is not an integer in range 4-16')


def get_display_word(word: str, hidden_word: str) -> str:
    """Get the word suitable for display."""
    if len(word) != len(hidden_word):
        raise ValueError('Word length and indices length are not the same')
    displayed_word = ''.join(
            [' ' + letter + ' ' if hidden_word[i] else' _ ' for i, letter in enumerate(word)])
    return displayed_word.strip()


def get_next_letter(remaining_letters: List):
    """Get the user-inputted next letter."""
    if len(remaining_letters) == 0:
        raise ValueError('There are no remaining letters')
    while True:
        next_letter = input('Choose the next letter: ').lower()
        if len(next_letter) != 1:
            print(f' {next_letter} is not a single character')
        elif next_letter not in ascii_lowercase:
            print(f' {next_letter}  is not a letter')
        elif next_letter not in remaining_letters:
            print(f' {next_letter} has been guessed before')
        else:
            remaining_letters.remove(next_letter)
        return next_letter


def play_hangman():
    """Play a game of hangman."""

    # Set difficulty
    print('Starting a game of Hangman...')
    attempts_remaining = get_users_attempt()
    min_word_length = get_min_word_length()

    # Randomly select a word
    print('Selecting a word...')
    word = get_random_word(min_word_length)
    print()

    # Game state variables
    hidden_word = [letter not in ascii_lowercase for letter in word]
    remaining_letters = set(ascii_lowercase)
    wrong_letters = []
    word_solved = False

    # Main game loop
    while attempts_remaining > 0 and not word_solved:
        # Print current game state
        print(f'Word: {get_display_word(word, hidden_word)}')
        print(f'Attempts Remaining: {attempts_remaining}')
        print(f"Wrong Letters: {' '.join(wrong_letters)}")
        print()

        # Get player's next letter guess
        next_letter = get_next_letter(remaining_letters)

        # Check if letter guess is in word
        if next_letter in word:
            print(f'{next_letter} is in the word!')
            for i in range(len(word)):
                if word[i] == next_letter:
                    hidden_word[i] = True
        else:
            print(f'{next_letter} is NOT in the word!')
            # Decrement num of attempts left and append guess to wrong guesses
            attempts_remaining -= 1
            wrong_letters.append(next_letter)

        # Check if word is completely solved
        if False not in hidden_word:
            word_solved = True
        print(f"You have won! Word: {word}")


if __name__ == "__main__":
    play_hangman()
