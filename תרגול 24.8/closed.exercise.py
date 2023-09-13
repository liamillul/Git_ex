name_of_the_employee = input("enter the new employee's name: ")
birthday = input("enter the new employee's birthday: ")
# condition for impossible month
if int(birthday[2:4]) > 12 or birthday[2:4] == "00":
    print("month can't be greater than 12 or 0")
# condition for impossible day, generally
if int(birthday[0:2]) > 31 or birthday[0:2] == "00":
    print("invalid day of birth")
# february limitations
if birthday[2:4] == "02":
    if int(birthday[0:2]) > 28:
        print("invalid day of birth, the max days in this month is 28")
    else:
        print(name_of_the_employee, "'s birthday is on", birthday[0:2], "/", birthday[2:4], "don't forget the cake:)")
# limitations for all month with 30 days max
elif int(birthday[0:2]) == 31:
    if birthday[2:4] == "04" or birthday[2:4] == "06" or birthday[2:4] == "09" or birthday[2:4] == "11":
        print("invalid day of birth, the max days in this month is 30")
    else:
        print(name_of_the_employee, "'s birthday is on", birthday[0:2], "/", birthday[2:4], "don't forget the cake:)")
else:
    print(name_of_the_employee, "'s birthday is on", birthday[0:2], "/", birthday[2:4], "don't forget the cake:)")
