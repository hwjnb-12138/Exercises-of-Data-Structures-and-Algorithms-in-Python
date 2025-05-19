# At the close of Section 2.4.1, we suggest a model in which the CreditCard
#  class supports a nonpublic method, _set_balance(b), that could be used
#  by subclasses to affect a change to the balance, without directly accessing
#  the _balance data member. Implement such a model, revising both the
#  CreditCard and PredatoryCreditCard classes accordingly.

class CreditCard:
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def _set_balance(self, new_balance):
        self._balance = new_balance

    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._set_balance(self._balance + price)
            return True

    def make_payment(self, amount):
        self._set_balance(self._balance - amount)


class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr

    def charge(self, price):
        success = super().charge(price)
        if not success:
            self._set_balance(self._balance + 5)
        return success

    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            new_balance = self._balance * monthly_factor
            self._set_balance(new_balance)
