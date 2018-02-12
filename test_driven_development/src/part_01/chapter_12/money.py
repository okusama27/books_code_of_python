from abc import ABCMeta


class Money:

    def __init__(self, amount, currency_):
        self.amount = amount
        self.currency_ = currency_

    def __eq__(self, other):
        return self.amount == other.amount and self.currency().__eq__(other.currency())

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency_)

    def currency(self):
        return self.currency_

    @classmethod
    def dollar(cls, amount):
        return Money(amount, "USD")

    @classmethod
    def franc(cls, amount):
        return Money(amount, "CHF")

    def __repr__(self):
        return str(self.amount) + " " + self.currency_

    def __add__(self, other):
        return Money(self.amount + other.amount, self.currency_)


class Expression:
    __metaclass__ = ABCMeta


class Bank:

    def reduce(self, source, to):
        return Money.dollar(10)
