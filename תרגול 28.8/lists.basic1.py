friends_list = ["inbar", "noy", "lihi", "liem", "noga"]
friends_list.append("adar")
print(friends_list[2])
for name in friends_list:
    if len(name) == 4:
        print(name)
print(len(friends_list))
new_name = str(input("what is your new name?: "))
friends_list[0] = new_name
friends_list.clear()
print(friends_list)
name1 = input("enter a first friend's name: ")
name2 = input("enter a second friend's name: ")
name3 = input("enter a third friend's name: ")
friends_list.insert(0, name1)
friends_list.insert(1, name2)
friends_list.insert(2, name3)
print(friends_list)
print(input("enter a name: ") in friends_list)
name4 = input("enter a name: ")
if name4 in friends_list:
    friends_list.remove(name4)
    print(friends_list)


