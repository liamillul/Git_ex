import random
list1 = [5, 4, 8, 1]
new_list = []
index_list = []
for num in list1:
    index = random.randrange(0, len(list1))
    while index in index_list:
        index = random.randrange(0, len(list1))
    index_list.append(index)
    new_list.append((list1[index]))
print("the new list: ", new_list)


