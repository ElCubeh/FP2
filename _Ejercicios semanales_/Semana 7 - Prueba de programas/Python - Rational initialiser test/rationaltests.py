"""Módulo de prueba de la clase Rational."""

import unittest
from rational import Rational


# Escriba su código aquí
class InitTests(unittest.TestCase):

    def test_positive_numerator_positive_denominator(self):
        r = Rational(3, 5)
        self.assertEqual(r.numerator, 3)
        self.assertEqual(r.denominator, 5)

    def test_positive_numerator_negative_denominator(self):
        r = Rational(3, -5)
        self.assertEqual(r.numerator, -3)
        self.assertEqual(r.denominator, 5)

    def test_negative_numerator_negative_denominator(self):
        r = Rational(-3, -5)
        self.assertEqual(r.numerator, 3)
        self.assertEqual(r.denominator, 5)

    def test_negative_numerator_positive_denominator(self):
        r = Rational(-3, 5)
        self.assertEqual(r.numerator, -3)
        self.assertEqual(r.denominator, 5)

    def test_zero_numerator_positive_denominator(self):
        r = Rational(0, 5)
        self.assertEqual(r.numerator, 0)
        self.assertEqual(r.denominator, 5)

    def test_zero_numerator_negative_denominator(self):
        r = Rational(0, -5)
        self.assertEqual(r.numerator, 0)
        self.assertEqual(r.denominator, 5)

    def test_zero_denominator_raises_value_error(self):
        with self.assertRaises(ValueError):
            Rational(3, 0)


if __name__ == "__main__":
    unittest.main()
