import random

WORDS = [
    "python", "computer", "program", "keyboard",
    "software", "student", "hangman", "science",
    "internet", "developer"
]

MAX_ATTEMPTS = 6

HANGMAN_STAGES = [
    r"""
      +---+
      |   |
          |
          |
          |
          |

    """,
    r"""
      +---+
      |   |
      O   |
          |
          |
          |

    """,
    r"""
      +---+
      |   |
      O   |
      |   |
          |
          |

    """,
    r"""
      +---+
      |   |
      O   |
     /|   |
          |
          |

    """,
    r"""
      +---+
      |   |
      O   |
     /|\  |
          |
          |

    """,
    r"""
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |

    """,
    r"""
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |

    """
]

def display_word(secret_word, guessed_letters):
    return " ".join(
        letter.upper() if letter in guessed_letters else "_"
        for letter in secret_word
    )

def play_game():
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = set()
    print("=" * 35)
    print("       HANGMAN WORD GAME")
    print("=" * 35)
    print("Guess the hidden word!")
    print("You have 6 incorrect attempts.")
    while len(wrong_guesses) < MAX_ATTEMPTS:
        print(HANGMAN_STAGES[len(wrong_guesses)])
        print("Word:", display_word(secret_word, guessed_letters))
        previous_guesses = sorted(guessed_letters | wrong_guesses)
        print("Guessed letters:", " ".join(letter.upper() for letter in previous_guesses) if previous_guesses else "None")
        print("Lives left:", MAX_ATTEMPTS - len(wrong_guesses))
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isascii() or not guess.isalpha():
            print("Please enter one English letter (A-Z).\n")
            continue
        if guess in guessed_letters or guess in wrong_guesses:
            print("You already guessed that letter. No penalty!\n")
            continue
        if guess in secret_word:
            guessed_letters.add(guess)
            print("Correct guess!\n")
            if all(letter in guessed_letters for letter in secret_word):
                print("Word:", display_word(secret_word, guessed_letters))
                print("\nCONGRATULATIONS! YOU WIN!")
                print("The secret word was:", secret_word.upper())
                return
        else:
            wrong_guesses.add(guess)
            print("Wrong guess! Try again.\n")
    print(HANGMAN_STAGES[MAX_ATTEMPTS])
    print("\nGAME OVER! YOU LOSE!")
    print("The secret word was:", secret_word.upper())

if __name__ == "__main__":
    play_game()