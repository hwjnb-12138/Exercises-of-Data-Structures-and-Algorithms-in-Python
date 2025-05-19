# Modify the declaration of the first for loop in the CreditCard tests, from
#  Code Fragment 2.3, so that it will eventually cause exactly one of the three
#  credit cards to go over its credit limit. Which credit card is it?

if __name__ == '__main__':
    wallet=[]
    wallet.append(CreditCard("JohnBowman", "CaliforniaSavings", 5391037593875309, 2500))
    wallet.append(CreditCard("JohnBowman", "CaliforniaFederal", 3485039933951954, 3500))
    wallet.append(CreditCard("JohnBowman", "CaliforniaFinance", 5391037593875309, 5000))

    for val in range(1, 1700):
        wallet[0].charge(val)
        wallet[1].charge(2 * val)
        wallet[2].charge(3 * val)

# The third one
