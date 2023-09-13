num = int(input("please enter a number, -1 to stop: "))
count = 0
s = " "
while num != -1:
    count += 1
    for num2 in range(1, num + 1):
        print(str(num2 * count))  # print the first row
    s += str(num2 * count)
    print(s)
#    for num2 in range(2, num + 1):
#         str(num * count * num2)) # for the last row

    num = int(input("please enter another number, -1 to stop: "))

print("game over")










