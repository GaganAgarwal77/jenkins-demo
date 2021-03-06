#!/usr/bin/python3
# Testing factorial of a number

import unittest
from program import factorial

class TestMean(unittest.TestCase):
    def test_mul1(self):
        result1 = factorial(5)
        self.assertEqual(result1, 120)
    def test_mul2(self):
        result2 = factorial(0)
        self.assertEqual(result2, 0)
    def test_mul3(self):
        result3 = factorial(10)
        self.assertEqual(result3, 1)


if __name__ == '__main__':
    unittest.main()
