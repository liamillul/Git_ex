SECRET_WORD_LIST = "lists"
WORD_LEN = len(SECRET_WORD_LIST)
is_finished = False


def len_guess(guess_):
    print()
    while len(guess_) != WORD_LEN:
        print("Your guess has", len(guess_), "letters and should have", WORD_LEN)
        print()
        guess_ = input("Enter guess: ")
    return guess_
# here there is a problem


def colors(guess_, secret_word):
    for index in range(len(guess_)):
        letter = guess_[index]
        if secret_word[index] == letter:
            green_list.append(letter)
        elif letter in secret_word:
            orange_list.append(letter)
        else:
            gray_list.append(letter)
    return len(green_list)


guess = input("Enter guess: ")
guess_new = len_guess(guess)  # ret1 is the updates guess


green_list = []
orange_list = []
gray_list = []

ret = colors(guess_new, SECRET_WORD_LIST)
if ret == WORD_LEN:
    is_finished = True
else:
    print("Green letters: ", green_list)
    print("Orange letters: ", orange_list)
    print("Gray letters: ", gray_list)

print("Congratulations!")
