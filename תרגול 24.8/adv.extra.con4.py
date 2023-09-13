ANIMAL = input("enter your animal type- dog or cat: ")
BUDGET = int(input("enter your budget for your pet food: "))

match ANIMAL:

    case "dog":
        if BUDGET < 20:
            print("you don't have enough money")
        elif 20 <= BUDGET < 40:
            print("you should buy basic food")
        elif BUDGET >= 40:
            print("you should buy expensive food")
    case "cat":
        if BUDGET < 50:
            print("you don't have enough money")
        elif 50 <= BUDGET < 100:
            print("you should buy basic food")
        elif BUDGET >= 100:
            print("you should buy expensive food")
