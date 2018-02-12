import unittest

from money import Bank
from money import Money
from money import Sum


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
        five = Money.dollar(5)
        sum = five.__add__(five)
        bank = Bank()
        reduced = bank.reduce(sum, "USD")
        self.assertEquals(Money.dollar(10), reduced)

    def test_plus_returns_sum(self):
        five = Money.dollar(5)
        sum = five.__add__(five)
        self.assertEquals(five, sum.augend)
        self.assertEquals(five, sum.addend)

    def test_reduce_sum(self):
        sum = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(sum, "USD")
        self.assertEquals(Money.dollar(7), result)

    def test_reduce_money(self):
        bank = Bank()
        result = bank.reduce(Money.dollar(1), "USD")
        self.assertEquals(Money.dollar(1), result)

    def test_reduce_money_different_currency(self):
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        result = bank.reduce(Money.franc(2), "USD")
        self.assertEquals(Money.dollar(1), result)

    def test_identity_rate(self):
        bank = Bank()
        self.assertEquals(1, bank.rate("USD", "USD"))

    def test_mixed_addition(self):
        five_bucks = Money.dollar(5)
        ten_francs = Money.franc(10)

        bank = Bank()
        bank.add_rate("CHF", "USD", 2)

        result = bank.reduce(five_bucks.__add__(ten_francs), "USD")
        self.assertEquals(Money.dollar(10), result)

    def test_sum_plus_money(self):
        five_bucks = Money.dollar(5)
        ten_francs = Money.franc(10)

        bank = Bank()
        bank.add_rate("CHF", "USD", 2)

        sum = Sum(five_bucks, ten_francs).__add__(five_bucks)
        result = bank.reduce(sum, "USD")
        self.assertEquals(Money.dollar(15), result)

    def test_sum_times(self):
        five_bucks = Money.dollar(5)
        ten_francs = Money.franc(10)

        bank = Bank()
        bank.add_rate("CHF", "USD", 2)

        sum = Sum(five_bucks, ten_francs).times(2)
        result = bank.reduce(sum, "USD")
        self.assertEquals(Money.dollar(20), result)

    # def test_plus_same_currency_returns_money(self):
    #     sum = Money.dollar(1).__add__(Money.dollar(1))
    #     self.assertTrue(isinstance(sum, Money))
