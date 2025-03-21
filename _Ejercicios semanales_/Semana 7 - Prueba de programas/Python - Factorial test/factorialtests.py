"""Módulo de pruebas de la clase Factorial."""

import unittest
import factorial


# Escriba su código aquí
class FactorialTests(unittest.TestCase):

    def test_1_positivo(self):
        self.assertEqual(factorial.Factorial(0), 1)
        self.assertEqual(factorial.Factorial(1), 1)
        self.assertEqual(factorial.Factorial(2), 2)
        self.assertEqual(factorial.Factorial(5), 120)
        self.assertEqual(factorial.Factorial(10), 3628800)

    def test_2_negativo(self):
        self.assertIsNone(factorial.Factorial(-1))
        self.assertIsNone(factorial.Factorial(-5))
        self.assertIsNone(factorial.Factorial(-10))

    def test_4_edge_values(self):
        self.assertEqual(factorial.Factorial(0), 1)
        self.assertEqual(factorial.Factorial(1), 1)
        self.assertIsNone(factorial.Factorial(-1))
        self.assertIsNone(factorial.Factorial(-2))


if __name__ == "__main__":
    unittest.main()
