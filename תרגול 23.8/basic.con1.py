account_amount = float(input("enter your account amount: "))
STOCK1 = 10
STOCK2 = 15

if account_amount >= 50000 and account_amount % STOCK1 == 0 or account_amount % STOCK2 == 0:
    print("Rock on!")
else:
    print("Can't invest")
