import unittest

from money import Bank
# from money import Expression
from money import Money


class MoneyTest(unittest.TestCase):

    def test_multiplication(self):
        five = Money.dollar(5)
        self.assertEquals(Money.dollar(10), five.times(2))
        self.assertEquals(Money.dollar(15), five.times(3))

    def test_equality(self):
        self.assertTrue(Money.dollar(5).__eq__(Money.dollar(5)))
        self.assertFalse(Money.dollar(5).__eq__(Money.dollar(6)))
        self.assertFalse(Money.franc(5).__eq__(Money.dollar(5)))

    def test_currency(self):
        self.assertEquals("USD", Money.dollar(1).currency())
        self.assertEquals("CHF", Money.franc(1).currency())

    def test_simple_addition(self):
        # sum = Money.dollar(5).__add__(Money.dollar(5))
        # self.assertEquals(Money.dollar(10), sum)
        five = Money.dollar(5)
        sum = five.__add__(five)
        bank = Bank()
        reduced = bank.reduce(sum, "USD")
        self.assertEquals(Money.dollar(10), reduced)
