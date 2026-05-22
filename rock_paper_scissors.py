import random as r

choice_pool = ("r", "p", "s")


def judge(a, b):
    if b == a:
        print("Tie!")
    elif (a == "r" and b == "p") or (a == "s" and b == "r") or (a == "p" and b == "s"):
        print(f"computer's choice is {b},you lose.")
    else:
        print(f"computer's choice is {b},you win.")


def whether():
    while True:
        whether_end = input("Would you want to try again?(y/n):").lower()
        if whether_end in ("y", "n"):
            break
        else:
            print("Invalid input!")
    return whether_end


while True:
    com_choice = r.choice(choice_pool)
    user_choice = input("Rock, Paper or Scissors?(r/p/s):").lower()

    if user_choice in choice_pool:
        judge(user_choice, com_choice)
        if whether() == "n":
            break
    else:
        print("Invalid input!")
