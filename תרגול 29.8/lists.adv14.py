list1 = []
length = int(input("enter the length of the list: "))
while length < 0:
    length = int(input("invalid length. enter another length of the list: "))
for val in range(length):
    list1.append(int(input("enter a value to the list: ")))
num_for_average_list = []
for i in range(0, length - 1):
    if list1[i] < list1[i + 1]:
        num_for_average_list.append(list1[i])
average = sum(num_for_average_list) / len(num_for_average_list)
print("the average is:", average)
