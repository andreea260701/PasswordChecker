# test_checker.py
import unittest
from passwordchecker.checker import evaluate_strength


class TestPasswordStrengthChecker(unittest.TestCase):

    def test_weak_password(self):
        self.assertEqual(evaluate_strength("abc"), "Parola este slabă")

    def test_medium_password(self):
        self.assertEqual(evaluate_strength("abcD123"), "Parola este medie")

    def test_strong_password(self):
        self.assertEqual(evaluate_strength("AbcD123!"), "Parola este puternică")


if __name__ == '__main__':
    unittest.main()
