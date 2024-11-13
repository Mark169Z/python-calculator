import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(5, 9), 14)

    # Add the following test methods to the TestCalculator class:
        
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 10), -5)
        self.assertEqual(self.calc.subtract(20, 10), 10)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 4), 20)
        self.assertEqual(self.calc.multiply(10, 4), 40)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 3), 3)
        self.assertEqual(self.calc.divide(20, 7), 2)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(31, 5), 1)
        self.assertEqual(self.calc.modulo(16, 2), 0)

if __name__ == '__main__':
    unittest.main()