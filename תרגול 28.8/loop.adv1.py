import random
num_of_players = int(input("enter the number of players: "))
for count in range(1, num_of_players + 1):
    random_num = (random.randrange(101))
    guess = int(input("player " + str(count) + " please enter your guess: "))
    if guess != random_num:
        if guess > random_num:
            guess = int(input("too high. try again: "))
        elif guess < random_num:
            guess = int(input("too low. try again: "))
        if guess == random_num:
            print("you won!")
        print("you had 2 guesses")
    elif guess == random_num:
        print("your guess is right. you won")
        print("your turn is over with 1 guess")
print("game over")
# with bonus 1
