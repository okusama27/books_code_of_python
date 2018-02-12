import unittest

from money import Dollar, Franc, Money


class MoneyTest(unittest.TestCase):

    def test_multiplication(self):
        five = Money.dollar(5)
        self.assertEquals(Money.dollar(10), five.times(2))
        self.assertEquals(Money.dollar(15), five.times(3))

    def test_equality(self):
        self.assertTrue(Money.dollar(5).__eq__(Money.dollar(5)))
        self.assertFalse(Money.dollar(5).__eq__(Money.dollar(6)))
        self.assertTrue(Money.franc(5).__eq__(Money.franc(5)))
        self.assertFalse(Money.franc(5).__eq__(Money.franc(6)))
        self.assertFalse(Money.franc(5).__eq__(Money.dollar(5)))

    def test_franc_multiplication(self):
        five = Money.franc(5)
        self.assertEquals(Money.franc(10), five.times(2))
        self.assertEquals(Money.franc(15), five.times(3))

    def test_currency(self):
        self.assertEquals("USD", Money.dollar(1).currency())
        self.assertEquals("CHF", Money.franc(1).currency())

    def test_different_class_equality(self):
        self.assertTrue(Money(10, "USD").__eq__(Dollar(10, "USD")))
        self.assertTrue(Money(10, "CHF").__eq__(Franc(10, "CHF")))
