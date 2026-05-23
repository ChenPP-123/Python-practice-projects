import random as r


def get_enter():
    while True:
        try:
            answer = int(
                input("Enter a number between 1 and 100 for computer to guess!:")
            )
            if 1 <= answer <= 100:
                return answer
            else:
                print("please make sure the number is between 1 and 100!")
        except ValueError:
            print("Invalid input!")


def get_response(computer_guess):
    while True:
        response = input(
            f"the computer's answer is {computer_guess}, is it too low(L), too high(H) or correct(C)?:"
        )
        if response in ("L", "H", "C"):
            return response
        else:
            print("Invalid input!")


answer = get_enter()

high = 100
low = 1

while True:
    computer_guess = r.randint(low, high)

    print(computer_guess)
    response = get_response(computer_guess)

    match response:
        case "L":
            if computer_guess < answer:
                low = computer_guess + 1
            else:
                print("Hey! Your responses are contradictory. Are you cheating?")
                break
        case "H":
            if computer_guess > answer:
                high = computer_guess - 1
            else:
                print("Hey! Your responses are contradictory. Are you cheating?")
                break
        case "C":
            print(f"answer is {computer_guess}!")
            break
