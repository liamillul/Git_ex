my_list = ["o", "hat", "aba", "1221", "umbrella", "pickup", "22.3.22"]
count = 0
for val in my_list:
    if len(val) > 1 and val[-1] == val[0]:
        count += my_list.count(val)
print("the amount of suitable values is:", count)

