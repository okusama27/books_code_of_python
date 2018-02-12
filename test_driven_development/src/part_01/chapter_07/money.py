class Money:

    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount and type(self) == type(other)


class Dollar(Money):

    def __init__(self, amount):
        super().__init__(amount)

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)


class Franc(Money):

    def __init__(self, amount):
        super().__init__(amount)

    def times(self, multiplier):
        return Franc(self.amount * multiplier)
