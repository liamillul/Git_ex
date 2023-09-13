my_list = [198, 76, 4, 2]
index = int(input("enter the index of the value you want to remove: "))
while index < 0 or index > 3:
    index = int(input("enter another index: "))
del my_list[index]
print("updated list:", my_list)
