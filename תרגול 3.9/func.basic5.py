def conditions(word):
    if word[0] == "A":
        if word[-1] == "Z":
            return "the word starts with 'A' and ends with 'Z'"
        else:
            return "the word starts with 'A'"
    else:
        if word[-1] == "Z":
            return "the word ends with 'Z'"
        else:
            return "the word does not start with 'A' and doesn't ends with 'Z'"


word1 = input("enter a word: ")
print(conditions(word1))
