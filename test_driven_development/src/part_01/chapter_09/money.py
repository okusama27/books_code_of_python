class Money:

    def __init__(self, amount, currency_):
        self.amount = amount
        self.currency_ = currency_

    def __eq__(self, other):
        return self.amount == other.amount and type(self) == type(other)

    def times(self, multiplier):
        pass

    def currency(self):
        return self.currency_

    @classmethod
    def dollar(cls, amount):
        return Dollar(amount, "USD")

    @classmethod
    def franc(cls, amount):
        return Franc(amount, "CHF")


class Dollar(Money):

    def __init__(self, amount, currency_):
        super().__init__(amount, currency_)

    def times(self, multiplier):
        return Money.dollar(self.amount * multiplier)

    def currency(self):
        return self.currency_


class Franc(Money):

    def __init__(self, amount, currency_):
        super().__init__(amount, currency_)

    def times(self, multiplier):
        return Money.franc(self.amount * multiplier)
