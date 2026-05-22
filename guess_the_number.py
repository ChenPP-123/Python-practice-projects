import random as r

tar = r.randint(1, 100)

while True:
    try:
        answ = int(input("Guess the number betwenn 1 and 100:"))
        if answ > tar:
            print("Too high!")
        elif answ < tar:
            print("Too low!")
        else:
            print("Correct!")
            break
    except ValueError:
        print("Invalid input! Please enter a valid number!")
