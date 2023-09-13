num1 = int(input("please enter a first number: "))
num2 = int(input("please enter a second number: "))
action = input("please enter an action between the two numbers: ")

if action == "+":
    print(num1 + num2)
if action == "-" and num1 - num2 > 0:
    print(num1 - num2)
if action == "*":
    print(num1 * num2)
elif action == "/":
    print(num1 / num2)
else:
    print("can't calculate")
