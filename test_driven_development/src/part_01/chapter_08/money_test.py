import unittest

from money import Money


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
