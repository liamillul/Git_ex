def new_list(numbers):
    return list(dict.fromkeys(numbers))


num_list = [1, 4, 8, 8, 5, 4, 9, 4]
new_list = new_list(num_list)
print(new_list)
