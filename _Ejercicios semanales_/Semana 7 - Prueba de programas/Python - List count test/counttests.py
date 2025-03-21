"""Módulo de pruebas de la función count."""

import unittest
from functions import count


# Escriba su código aquí
class CountTests(unittest.TestCase):
    def test_count_value_present(self):
        self.assertEqual(count([1, 2, 3, 2, 4, 2], 2), 3)

    def test_count_value_not_present(self):
        self.assertEqual(count([1, 2, 3, 4], 5), 0)

    def test_count_empty_list(self):
        self.assertEqual(count([], 1), 0)

    def test_count_single_element_list(self):
        self.assertEqual(count([1], 1), 1)
        self.assertEqual(count([1], 2), 0)

    def test_count_strings(self):
        self.assertEqual(count(["a", "b", "a", "c"], "a"), 2)

    def test_count_mixed_types(self):
        self.assertEqual(count([1, "1", 1.0, True], 1), 3)

    def test_count_value_first(self):
        self.assertEqual(count([2, 3, 4, 5], 2), 1)

    def test_count_value_last(self):
        self.assertEqual(count([3, 4, 5, 6], 6), 1)

    def test_count_value_middle(self):
        self.assertEqual(count([1, 2, 3, 4, 5], 3), 1)

    def test_count_all_except_first(self):
        self.assertEqual(count([1, 2, 2, 2], 2), 3)

    def test_count_all_except_last(self):
        self.assertEqual(count([2, 2, 2, 1], 2), 3)

    def test_count_all_elements_same(self):
        self.assertEqual(count([3, 3, 3, 3], 3), 4)


if __name__ == "__main__":
    unittest.main()
