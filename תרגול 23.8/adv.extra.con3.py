SPARKLING_DRINK = input("do you want a sparkling drink? enter yes/no: ")
SWEET_DRINK = input("do you want a sweet drink? enter yes/no: ")

if SPARKLING_DRINK == "yes":
    if SWEET_DRINK == "no":
        print("your drink is soda")
    elif SWEET_DRINK == "yes":
        print("your drink is coke")
elif SPARKLING_DRINK == "no":
    if SWEET_DRINK == "yes":
        print("your drink is raspberry")
    elif SWEET_DRINK == "no":
        print("your drink is water")
