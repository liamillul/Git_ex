my_list = [7, -40.3, "hello", 222, '+']
for val in my_list:
    if type(val) == int:
        print("the value", val, "is an integer")
    elif type(val) == float:
        print("the value", val, "is a float")
    else:
        print("the value", val, "is a string")
