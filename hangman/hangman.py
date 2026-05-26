import random
from words import words
from hangman_visual import lives_visual_dict
import string


def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()


def hangman(lives: int = 7):

    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0 and lives > 0:
        print("-" * 100)
        print(
            "You have",
            lives,
            "lives,and you have used these letters:",
            " ".join(used_letters),
        )
        print(lives_visual_dict[lives])
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word:", " ".join(word_list))

        user_letter = input("Guess a letter:").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                print("This letter is not in the word")
                lives -= 1

        elif user_letter in used_letters:
            print("You have already used that one, please try anotherone.")
        else:
            print("Invalid charactor, please try again.")

    if len(word_letters) == 0:
        print(
            "The word is :",
            " ".join([letter if letter in used_letters else "-" for letter in word]),
        )
    else:
        print("You die, the word is", word)


hangman()
