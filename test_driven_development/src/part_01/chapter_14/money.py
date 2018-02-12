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

    def reduce(self, bank, to):
        # return self
        # rate = 1
        # if self.currency_.__eq__("CHF") and to.__eq__("USD"):
        #     rate = 2
        rate = bank.rate(self.currency_, to)
        return Money(self.amount / rate, to)


class Expression:
    __metaclass__ = ABCMeta

    def reduce(self, bank, to):
        pass


class Bank:

    def __init__(self):
        self.rates = {}

    def reduce(self, source, to):
        # if isinstance(source, Money):
        #     return source.reduce(to)
        # return Money.dollar(10)
        # sum = source
        # amount = sum.augend.amount + sum.addend.amount
        # return Money(amount, to)
        return source.reduce(self, to)

    def add_rate(self, from_, to, rate_):
        pair = Pair(from_, to)
        self.rates[pair.make_tuple()] = rate_

    def rate(self, from_, to):
        # rate = 1
        # if from_.__eq__("CHF") and to.__eq__("USD"):
        #     rate = 2
        if from_.__eq__(to):
            return 1
        pair = Pair(from_, to)
        return self.rates.get(pair.make_tuple())


class Sum(Exception):

    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank, to):
        amount = self.augend.amount + self.addend.amount
        return Money(amount, to)


class Pair:

    def __init__(self, from_, to):
        self.from_ = from_
        self.to = to

    def __eq__(self, other):
        pair = other
        return self.from_.__eq__(pair.from_) and self.to.__eq__(pair.to)

    def hash_code(self):
        return 0

    def make_tuple(self):
        return (self.from_, self.to)