def first_letter(word):
    if word[0] == "A":
        return True
    else:
        return False


word_ = input("enter a word: ")
print("is the word begins with 'A'?", first_letter(word_))
