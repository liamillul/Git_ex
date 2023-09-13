summary = 0
count = 0
num1 = int(input("enter a number: "))
while num1 != -1:
    summary += num1
    count += 1
    num1 = int(input("enter a number: "))
if summary == 0 or count == 0:
    print("invalid, please enter a different number")
else:
    print(summary / count)
