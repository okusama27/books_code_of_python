import unittest

from money import Dollar, Franc


class MoneyTest(unittest.TestCase):

    def test_multiplication(self):
        five = Dollar(5)
        # product = five.times(2)
        self.assertEquals(Dollar(10), five.times(2))
        # product = five.times(3)
        self.assertEquals(Dollar(15), five.times(3))

    def test_equality(self):
        self.assertTrue(Dollar(5).__eq__(Dollar(5)))
        self.assertFalse(Dollar(5).__eq__(Dollar(6)))
        self.assertTrue(Franc(5).__eq__(Franc(5)))
        self.assertFalse(Franc(5).__eq__(Franc(6)))

    def test_franc_multiplication(self):
        five = Franc(5)
        self.assertEquals(Franc(10), five.times(2))
        self.assertEquals(Franc(15), five.times(3))
