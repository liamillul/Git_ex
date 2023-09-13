shopping_list = ["eggs", "milk", "chocolate", "banana", "salt", "chips"]
prices_dict = {
 "eggs": 20.2,
 "yogurt": 5,
 "cheese": 20,
 "milk": 6.75,
 "chocolate": 15.5,
 "cornflakes": 25.3,
 "banana": 2,
 "apple": 3.1,
 "salt": 1.8,
 "chips": 13}
BUDGET = 50
shopping_list_prices = []
for product in shopping_list:
    if product in prices_dict:
        shopping_list_prices.append(prices_dict[product])
print("the amount of ALL the products in the shopping list is:", sum(shopping_list_prices))
shopping_list_sum = sum(shopping_list_prices)
change_dict = {}
possible_product_to_remove_list = []
for price in shopping_list_prices:
    if shopping_list_sum - price < BUDGET:
        # make a list of possible products to remove, took out the key by the value
        possible_product_to_remove_list = [k for k, v in prices_dict.items() if v == price]
        purchase_sum_without_p = shopping_list_sum - price
        for word in possible_product_to_remove_list:
            change_dict[word] = BUDGET - purchase_sum_without_p
print(change_dict)




