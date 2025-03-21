"""Módulo de pruebas de la función check_pass_len."""

import unittest
import functions


# Escriba su código aquí
class PasswlenTests(unittest.TestCase):

    def test_1_valido(self):
        self.assertTrue(functions.check_pass_len("password123"))

    def test_2_corto(self):
        self.assertFalse(functions.check_pass_len("pass"))
        self.assertFalse(functions.check_pass_len("p"))
        self.assertFalse(functions.check_pass_len(""))

    def test_3_largo(self):
        self.assertFalse(functions.check_pass_len("thisisaverylongpassword"))

    def test_4_edge(self):
        self.assertTrue(functions.check_pass_len("abcdefgh"))
        self.assertTrue(functions.check_pass_len("abcdefghi"))
        self.assertTrue(functions.check_pass_len("abcdefghiklmno"))
        self.assertTrue(functions.check_pass_len("abcdefghiklmn"))

    def test_5_near_edge(self):
        self.assertFalse(functions.check_pass_len("abcdefg"))
        self.assertFalse(functions.check_pass_len("abcdef"))
        self.assertFalse(functions.check_pass_len("abcdefghijklmnop"))
        self.assertFalse(functions.check_pass_len("abcdefghijklmnopq"))


if __name__ == "__main__":
    unittest.main()
