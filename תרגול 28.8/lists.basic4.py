my_list = ["orange", "banana", "apple", "kiwi"]
index = int(input("enter an index: "))
while index < 0 or index > 4:
    index = int(input("please enter another index: "))
my_list.insert(index, "pineapple")
print(my_list)
