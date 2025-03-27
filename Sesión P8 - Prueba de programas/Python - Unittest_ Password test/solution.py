"""Módulo de pruebas de la función check_pass."""

import unittest
from functions import check_pass


# Escriba su código aquí
class PasswTests(unittest.TestCase):
    def test_valid_passwords(self):
        valid_passwords = [
            'Aa1bcdef',          # 8 characters, all requirements met
            'A1b2C3d4E5f',       # 11 characters
            'Aa123456789BCDE',   # 15 characters
        ]
        for password in valid_passwords:
            with self.subTest(password=password):
                self.assertTrue(check_pass(password))

    def test_invalid_length(self):
        invalid_passwords = [
            ('', 0),
            ('Aa1', 3),
            ('Aa1bcde', 7),
            ('Aa1bcdefghijklmnop', 16),
            ('Aa1bcdefghijklmnoPQRSTUV', 20),
        ]
        for password, length in invalid_passwords:
            with self.subTest(password=password, length=length):
                self.assertFalse(check_pass(password))

    def test_no_lowercase(self):
        passwords = [
            'ABCDEFG1',          # 8 characters, uppercase and digit
            'A1234567890BCDEF',  # 15 characters
            'AA11BB22CC33DD',    # 14 characters
        ]
        for password in passwords:
            with self.subTest(password=password):
                self.assertFalse(check_pass(password))

    def test_no_uppercase(self):
        passwords = [
            'abcdefg1',          # 8 characters, lowercase and digit
            'a1234567890bcdef',  # 15 characters
            'aa11bb22cc33dd',    # 14 characters
        ]
        for password in passwords:
            with self.subTest(password=password):
                self.assertFalse(check_pass(password))

    def test_no_digit(self):
        passwords = [
            'Abcdefgh',          # 8 characters, upper and lower
            'Abcdefghijklmno',   # 15 characters
            'aBcDeFgHiJkLmN',   # 14 characters
        ]
        for password in passwords:
            with self.subTest(password=password):
                self.assertFalse(check_pass(password))



if __name__ == "__main__":
    unittest.main()
