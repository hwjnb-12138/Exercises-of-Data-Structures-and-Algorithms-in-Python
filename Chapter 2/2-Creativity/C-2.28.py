# The PredatoryCreditCard class of Section 2.4.1 provides a process_month
#  method that models the completion of a monthly cycle. Modify the class
#  so that once a customer has made ten calls to charge in the current month,
#  each additional call to that function results in an additional $1 surcharge.

class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self._charge_calls = 0

    def charge(self, price):
        self._charge_calls += 1

        success = super().charge(price)
        if not success:
            self._balance += 5

        if self._charge_calls > 10:
            self._balance += 1

        return success

    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor

        self._charge_calls = 0
