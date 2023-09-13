from collections import Counter
my_list = [777, 543, 10, 22, 543, 10, 777, 22, 543, 21, 21, 777, 10, 81, 777]
# first path - no dictionary
for num in my_list:
    count = Counter(my_list)
print("the number is", max(count))
print("this number appears", count[max(count)], "times")
# gap
print("the second way:\n")
# second path - with dictionary
my_dict = Counter(my_list)
max_key = max(my_dict)
print("the number is", max_key)
max_times = max(my_dict.values())
print("this number appears", max_times, "times")

