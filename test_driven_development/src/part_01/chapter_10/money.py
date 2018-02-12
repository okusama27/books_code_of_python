class Money:

    def __init__(self, amount, currency_):
        self.amount = amount
        self.currency_ = currency_

    def __eq__(self, other):
        # return self.amount == other.amount and type(self) == type(other)
        return self.amount == other.amount and self.currency().__eq__(other.currency())

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency_)

    def currency(self):
        return self.currency_

    @classmethod
    def dollar(cls, amount):
        return Dollar(amount, "USD")

    @classmethod
    def franc(cls, amount):
        return Franc(amount, "CHF")

    def __repr__(self):
        return str(self.amount) + " " + self.currency_


class Dollar(Money):

    def __init__(self, amount, currency_):
        super().__init__(amount, currency_)


class Franc(Money):

    def __init__(self, amount, currency_):
        super().__init__(amount, currency_)


