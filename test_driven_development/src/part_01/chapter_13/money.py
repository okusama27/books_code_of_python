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
        return Sum(self, other)

    def reduce(self, to):
        return self


class Expression:
    __metaclass__ = ABCMeta

    def reduce(self, to):
        pass


class Bank:

    def reduce(self, source, to):
        # if isinstance(source, Money):
        #     return source.reduce(to)
        # return Money.dollar(10)
        # sum = source
        # amount = sum.augend.amount + sum.addend.amount
        # return Money(amount, to)
        return source.reduce(to)


class Sum(Exception):

    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, to):
        amount = self.augend.amount + self.addend.amount
        return Money(amount, to)
