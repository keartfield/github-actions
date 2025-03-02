import unittest
from python.main import EvenOrOdd

"""
python -m unittest python/main_test.py
"""
class TestEvenOrOdd(unittest.TestCase):
    def test_even(self):
        self.assertEqual(EvenOrOdd(2), "even")

    def test_odd(self):
        self.assertEqual(EvenOrOdd(3), "odd")

    def test_even_with_zero(self):
        self.assertEqual(EvenOrOdd(0), "even")

    def test_minus_even(self):
        self.assertEqual(EvenOrOdd(-2), "even")

    def test_minus_odd(self):
        self.assertEqual(EvenOrOdd(-3), "odd")


if __name__ == "__main__":
    unittest.main()
