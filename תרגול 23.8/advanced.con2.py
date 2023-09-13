MONEY_AMOUNT = int(input("enter how much money do you have: "))
NUM_OF_STOCKS = int(input("enter how many stocks you want to buy: "))
# CLASS A
if 1 <= MONEY_AMOUNT <= 10000:
    if 1 < NUM_OF_STOCKS <= 500:  # CLASS A1
        base_commissionA1 = 150
        special_commissionA1 = 80
        total_commission_A1 = base_commissionA1 + special_commissionA1
        print("the total commission you will pay is :", total_commission_A1)
    if 500 < NUM_OF_STOCKS:  # CLASS A2
        base_commissionA2 = 150
        special_commissionA2 = 70
        total_commission_A2 = base_commissionA2 + special_commissionA2
        print("the total commission you will pay is :", total_commission_A2)
# CLASS B
elif 10000 < MONEY_AMOUNT <= 50000:
    if 1 < NUM_OF_STOCKS <= 250:  # CLASS B1
        base_commissionB1 = 130
        special_commissionB1 = 40
        total_commission_B1 = base_commissionB1 + special_commissionB1
        print("the total commission you will pay is :", total_commission_B1)
    if 250 < NUM_OF_STOCKS:  # CLASS B2
        base_commissionB2 = 130
        special_commissionB2 = 30
        total_commission_B2 = base_commissionB2 + special_commissionB2
        print("the total commission you will pay is :", total_commission_B2)
# CLASS C
elif 50000 < MONEY_AMOUNT:
    base_commissionC = 110
    special_commissionC = 10
    total_commission_C = base_commissionC + special_commissionC
    print("the total commission you will pay is :", total_commission_C)
