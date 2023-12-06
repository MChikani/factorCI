import unittest
from src.fractions import Fraction

class TestFractions(unittest.TestCase):
    def test_fraction_show(self):
        x = Fraction(1, 2) 
        self.assertEqual(x.show(), "1/2")

    def test_fraction_str(self):
        y = Fraction(2, 3)
        self.assertEqual(str(y), "2/3")

    def test_fraction_eq(self):
        z = Fraction(3, 6)
        self.assertEqual(z, Fraction(1, 2))

    def test_fraction_add(self):
        x = Fraction(1, 2)
        y = Fraction(2, 3)
        result = x + y
        self.assertEqual(result, Fraction(7, 6))

    def test_fraction_get_num(self):
        x = Fraction(1, 2)
        self.assertEqual(x.get_num(), 1)

    def test_fraction_get_den(self):
        y = Fraction(2, 3)
        self.assertEqual(y.get_den(), 3)

    def test_fraction_sub(self):
        x = Fraction(1, 2)
        y = Fraction(2, 3)
        result = x - y
        self.assertEqual(result, Fraction(-1, 6))

    def test_fraction_mul(self):
        x = Fraction(1, 2)
        y = Fraction(2, 3)
        result = x * y
        self.assertEqual(result, Fraction(1, 3))

    def test_fraction_truediv(self):
        x = Fraction(1, 2)
        y = Fraction(2, 3)
        result = x / y
        self.assertEqual(result, Fraction(3, 4))

    def test_fraction_gt(self):
        x = Fraction(1, 2)
        y = Fraction(2, 3)
        self.assertFalse(x > y)

    def test_fraction_ge(self):
        x = Fraction(1, 2)
        y = Fraction(2, 3)
        self.assertFalse(x >= y)

    def test_fraction_lt(self):
        x = Fraction(1, 2)
        y = Fraction(2, 3)
        self.assertTrue(x < y)

    def test_fraction_le(self):
        x = Fraction(1, 2)
        y = Fraction(2, 3)
        self.assertTrue(x <= y)

    def test_fraction_ne(self):
        x = Fraction(1, 2)
        y = Fraction(2, 3)
        self.assertTrue(x != y)

    def test_fraction_constructor_type_error(self):
        with self.assertRaises(TypeError):
            Fraction(1.2, 2.2)

    def test_fraction_negative_denominator(self):
        beta = Fraction(3, -5)
        self.assertEqual(beta, Fraction(-3, 5))

    def test_fraction_radd(self):
        x = Fraction(1, 2)
        result = x + 1
        self.assertEqual(result, Fraction(3, 2))
 
if __name__ == "__main__":
    unittest.main()
