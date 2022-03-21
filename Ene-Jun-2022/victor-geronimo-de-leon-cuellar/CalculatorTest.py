import unittest

from Calculator import Calculator

class CalculatorTest(unittest, unittest.TestCase):
    def test_create_calculator(self):
        c = Calculator()
        self.assertIsInstance(c, Calculator)

    def test_input(self):
        pass

    def test_sum(self):
        pass

    def test_substract(self):
        pass

    def test_multiply(self):
        pass

    def test_divide(self):
        pass
    

if __name__ == "__main__":
    unittest.maini()