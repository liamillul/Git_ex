my_list = [11, 7, 3, 21, 4, 15]
num = int(input("enter the number of the player who left: "))
if num in my_list:
    my_list.remove(num)
    print("the new list:", my_list)
