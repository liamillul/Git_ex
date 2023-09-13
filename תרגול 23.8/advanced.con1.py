card1 = int(input("enter the first card number: "))
card2 = int(input("enter the second card number: "))
ACE = 1
# when the two cards are not ace
if card1 != ACE and card2 != ACE:
    if card1 > card2:
        print("player 1 has won")
    if card2 > card1:
        print("player 2 has won")
# when one of the cards is an ace
if card1 == ACE and card2 != ACE:
    print("player 1 has won")
if card2 == ACE and card1 != ACE:
    print("player 2 has won")
# until now everything is good
# tie situation
if card1 == card2:
    print("tie")
# another round
card1 = int(input("enter the first number in the second round: "))
card2 = int(input("enter the second number in the second round: "))
# 2nd round, when one of the cards is an ace
if card1 == ACE and card2 != ACE:
    print("player 1 has won")
elif card2 == ACE and card1 != ACE:
    print("player 2 has won")
# when both of the cards are not ace in the 2nd round
elif card1 != ACE and card2 != ACE:
    if card1 > card2 and card1 - card2 <= 2:
        print("player 1 has won")
    elif card2 > card1 and card2 - card1 <= 2:
        print("player 2 has won")
    else:
        print("it is a tie")
