day_of_the_week = int(input("enter the day you would like to come to the pool: "))
if day_of_the_week < 1 or day_of_the_week > 7:
    day_of_the_week = int(input("invalid day, please enter a number between 1-7: "))
hour = int(input("enter your arrival time: "))
purpose = int(input("enter a purpose- 1 is for swimming, 2 is for wading: "))
# week days except for wednesday
if 1 <= day_of_the_week < 4 or day_of_the_week == 5:
    if 700 <= hour <= 1100:
        if purpose == 1:
            print("you can come to the pool for swimming")
        elif purpose == 2:
            print("you can't come to the pool for wading")
    elif 1100 <= hour <= 2100:
        if purpose == 1:
            print("you can't come to the pool for swimming")
        elif purpose == 2:
            print("you can come to the pool for wading")
    elif hour < 700 or hour > 2100:
        print("the pool is closed")
# wednesday only
elif day_of_the_week == 4:
    if 700 <= hour <= 1100:
        if purpose == 1:
            print("you can come to the pool for swimming")
        elif purpose == 2:
            print("you can't come to the pool for wading")
    if 1100 <= hour <= 2100:
        if hour == 1500:
            print("the pool is closed for cleaning")
        else:
            if purpose == 1:
                print("you can't come to the pool for swimming")
            elif purpose == 2:
                print("you can come to the pool for wading")
    if hour < 700 or hour > 2100:
        print("the pool is closed")
# friday and saturday
elif 5 <= day_of_the_week <= 6:
    if 800 <= hour <= 1000:
        if purpose == 1:
            print("you can come to the pool for swimming")
        elif purpose == 2:
            print("you can't come to the pool for swimming")
    elif 1000 <= hour <= 1400:
        if purpose == 1:
            print("you can't come to the pool for swimming")
        elif purpose == 2:
            print("you can come to the pool for wading")
    elif hour < 800 or hour > 1400:
        print("the pool is closed")
