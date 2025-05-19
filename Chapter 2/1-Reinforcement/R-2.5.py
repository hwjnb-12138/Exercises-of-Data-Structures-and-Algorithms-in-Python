# Use the techniques of Section 1.7 to revise the charge and make_payment
#  methods of the CreditCard class to ensure that the caller sends a number
#  as a parameter.

class CreditCard:

    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def charge(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("price must be a numeric type.")
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("amount must be a numeric type.")
        self._balance -= amount
