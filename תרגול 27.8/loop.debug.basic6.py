print("Welcome to the meal calculator!")
print("What is the average price of a dish?")
dish_price = int(input())
# okay
print("How many dishes shall we have?")
dishes = int(input())
# okay
print("How many families are attending?")
families = int(input())
# okay
total_price = 0
family_sum = 0
# okay

for family_num in range(1, families + 1):
    print("family", family_num, ":")

    for dish_num in range(1, dishes + 1):
        print("How much of dish", dish_num, "did family", family_num,
              "ordered?")
        how_much_of_dish = int(input())
        if dish_num > 1:
            family_sum += dish_price * how_much_of_dish
        else:
            family_sum = dish_price * how_much_of_dish

        print("family", family_num, "will cost a total of", family_sum)

    total_price += family_sum

print("the total price of the dinner will be", total_price)