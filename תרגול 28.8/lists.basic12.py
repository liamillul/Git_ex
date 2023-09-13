num_list = [1, 7, 2, 4, 10]
uneven_num_list = []
for i in range(len(num_list)):
    if i % 2 != 0:
        uneven_num = num_list[i]
        uneven_num_list.append(uneven_num)
print(max(uneven_num_list))








