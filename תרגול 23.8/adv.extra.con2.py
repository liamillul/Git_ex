NUM_OF_PENCILS = int(input("how many pencils you want to buy: "))
PRICE_PER_PENCIL = 0.5
total_price = NUM_OF_PENCILS * PRICE_PER_PENCIL
if NUM_OF_PENCILS < 50:
    print("you cant buy any. the quantity is too low")
elif 50 < NUM_OF_PENCILS < 400:
    print("the price is: ", total_price)
elif 400 < NUM_OF_PENCILS:
    discount = 0.1 * total_price
    total_price_after_discount = total_price - discount
    print("the price is: ", total_price_after_discount)

