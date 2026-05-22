import random as r

re_counter = {}

while True:
    answer = input("rolling a dice?(y/n)").lower()
    if answer == "y":
        try:
            dice_num = int(input("How many dices do you want to roll?:"))
            results = [r.randint(1, 6) for _ in range(dice_num)]
            for dice in results:
                re_counter[dice] = re_counter.get(dice, 0) + 1
            out = ",".join(map(str, results))
            print(f"({out})")
        except ValueError:
            print("Please enter a number!")
    elif answer == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid input!")
print(f"statistic:{dict(sorted(re_counter.items(), reverse=True))}")
