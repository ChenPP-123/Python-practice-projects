import random as r

Rock = "r"
Paper = "p"
Scissors = "s"
choice_pool = (Rock, Paper, Scissors)


def judge(a, b):
    if b == a:
        print("Tie!")
    elif (
        (a == Rock and b == Paper)
        or (a == Scissors and b == Rock)
        or (a == Paper and b == Scissors)
    ):
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
