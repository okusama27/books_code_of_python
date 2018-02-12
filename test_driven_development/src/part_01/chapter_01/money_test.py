import unittest


class MoneyTest(unittest.TestCase):

    def test_multiplication(self):
        five = Dollar(5)
        five.times(2)
        self.assertEquals(10, five.amount)


class Dollar:

    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        self.amount *= multiplier
