"""Módulo de pruebas de la función count_pairs."""

import unittest
from functions import count_pairs


# Escriba su código aquí
class CountTests(unittest.TestCase):
    def test_lista_vacia(self):
        self.assertEqual(count_pairs([]), 0)

    def test_elemento_unico(self):
        self.assertEqual(count_pairs([69]), 0)

    def test_dos_elementos_iguales(self):
        self.assertEqual(count_pairs([3, 3]), 1)

    def test_dos_elementos_diferentes(self):
        self.assertEqual(count_pairs([3, 4]), 0)

    def test_todos_iguales(self):
        self.assertEqual(count_pairs([2] * 100), 99)

    def test_sin_parejas(self):
        self.assertEqual(count_pairs([1, 69, 2, 420, 4]), 0)

    def test_dos_elementos_iguales_principio(self):
        self.assertEqual(count_pairs([1, 1, 2, 3, 4]), 1)

    def test_dos_elementos_iguales_final(self):
        self.assertEqual(count_pairs([1, 2, 3, 4, 4]), 1)


if __name__ == "__main__":
    unittest.main()
