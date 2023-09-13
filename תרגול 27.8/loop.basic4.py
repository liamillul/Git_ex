num = float(input("enter a number: "))
power = 0
while num > 0:
    power += 1
    if num ** power < 500:
        print(num ** power)
    else:
        break
