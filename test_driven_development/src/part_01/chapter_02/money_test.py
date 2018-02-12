import unittest


class MoneyTest(unittest.TestCase):

    def test_multiplication(self):
        five = Dollar(5)
        product = five.times(2)
        self.assertEquals(10, product.amount)
        product = five.times(3)
        self.assertEquals(15, product.amount)


class Dollar:

    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        # self.amount *= multiplier
        return Dollar(self.amount * multiplier)
