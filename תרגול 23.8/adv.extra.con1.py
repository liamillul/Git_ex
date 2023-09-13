NUM = int(input("enter a number: "))
# THE NUM IS DIVIDED BY 3 AND BY 2
if NUM % 3 == 0 and NUM % 2 == 0:
    print("the number is divided by 3 and by 2")
# THE NUM IS DIVIDED JUST BY 3
elif NUM % 3 == 0 and NUM % 2 != 0:
    print("the number is divided only by 3")
# THE NUM IS DIVIDED JUST BY 2
elif NUM % 3 != 0 and NUM % 2 == 0:
    print("the number is divided only by 2")
