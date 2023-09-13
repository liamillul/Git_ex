def even_or_not(words):
    if len(words) % 2 == 0:
        print("the list length is even")
    else:
        print("the list length is not even")
    return len(words)


words_list = ["lia", "cow", "dog", "rainbow"]
print(even_or_not(words_list))
