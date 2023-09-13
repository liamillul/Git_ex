HARRY_CARD = int(input("enter Harry's card number: "))
RON_CARD = int(input("enter Ron card number: "))
HERMIONE_CARD = int(input("enter Hermione card number: "))

if HERMIONE_CARD + HARRY_CARD == RON_CARD or HERMIONE_CARD + RON_CARD == HARRY_CARD or RON_CARD + HARRY_CARD == HERMIONE_CARD:
    print("the winner card is: ", min(HERMIONE_CARD, HARRY_CARD, RON_CARD))
if HERMIONE_CARD == HARRY_CARD == RON_CARD:
    print("tie")
else:
    print("the winner card is: ", max(HERMIONE_CARD, HARRY_CARD, RON_CARD))
