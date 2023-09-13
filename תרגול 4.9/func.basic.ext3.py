import random

# function 1 = random 3 steps
steps_list = ["right", "left"]


def is_step_seq(steps_):
    return random.choices(steps_, k=3)


def guess_of_steps(guess_):
    count = 0
    while guess_ != steps:
        guess_ = list(input("try again. enter your guess: "))
        count += 1
    return count


steps = is_step_seq(steps_list)
guess = input("enter your guess: ")
guess = guess.split()
num_of_tries = guess_of_steps(guess)
print("You’ve lost", num_of_tries, "times but you did it, you are the WINNER!")
