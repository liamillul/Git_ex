def sub_string():
    for string in list1:
        cur_index = 0
        check = True
        for i in range(len(string)):
            if string[i] in WORD:
                if cur_index <= WORD.index(string[i]):
                    cur_index = WORD.index(string[i])
                else:
                    check = False
        if check:
            sub_string_list.append(string)


# current index is the index of the letter (in the sub-string) in the WORD!
# when the index in the WORD of the current letter is larger than the index of the letter we checked before, it is good.


def get_max_string(lst):
    return len(max(lst, key=len))


WORD = "computer"
list1 = ["com", "pmo", "cpter", "cpmuter"]
sub_string_list = []
sub_string()
print(get_max_string(sub_string_list))
