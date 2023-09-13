# 1
list1 = [3, 5, 45, 97, 32, 22, 10, 19, 39, 43]
even_num_list = [num for num in list1 if num % 2 == 0]
print(even_num_list)
# 2
list2 = [2, 3.75, 0.04, 59.354, 6, 7.777, 8, 9]
int_list = [num for num in list2 if type(num) == int]
print(int_list)
# 3
total_list = list(range(1, 1001))
new_list = [num for num in total_list if "3" in str(num)]
print(new_list)





