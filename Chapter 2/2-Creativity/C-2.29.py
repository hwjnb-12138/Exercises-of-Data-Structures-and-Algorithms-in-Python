# Modify the PredatoryCreditCard class from Section 2.4.1 so that a customer is
# assigned a minimum monthly payment, as a percentage of the balance, and so that
# a late fee is assessed if the customer does not subsequently pay that minimum
# amount before the next monthly cycle.

class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self._monthly_payment = 0
        self._min_payment_ratio = 0.05
        self._current_payment = 0

    def charge(self, price):
        success = super().charge(price)
        if not success:
            self._balance += 5
        return success

    def make_payment(self, payment):
        super().make_payment(payment)
        self._current_payment += payment

    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor

        if self._current_payment < self._monthly_payment:
            self._balance += 25

        self._monthly_payment = self._balance * self._min_payment_ratio
        self._current_payment = 0
