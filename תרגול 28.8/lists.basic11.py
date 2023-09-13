LIST = [12, 3, 5, 2, 4, 1]
count = 0
summary = 0
for num in LIST:
    while num % 2 == 0:
        summary += num
        count += 1
        break
print("the average of the even numbers is:", summary / count)













