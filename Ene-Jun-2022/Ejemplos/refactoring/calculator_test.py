import unittest

from calculator import Calculator

class CalculatorTest(unittest.TestCase):
    def test_create_calculator(self):
        c = Calculator()
        self.assertIsInstance(c, Calculator)
        
        c2 = Calculator(5, 6)
        self.assertIsInstance(c, Calculator)
    
    def test_input(self):
        c = Calculator(5, 6)
        self.assertIsInstance(c.get_a(), int)
        self.assertIsInstance(c.get_b(), int)
        self.assertEqual(c.get_a(), 5)
        self.assertEqual(c.get_b(), 6)
        
        c.set_a(7)
        c.set_b(8)
        self.assertEqual(c.get_a(), 7)
        self.assertEqual(c.get_b(), 8)
    
    def test_sum(self):
        c = Calculator(5, 6)
        result = c.sum()
        self.assertEqual(result, 11)
        self.assertIsInstance(result, int)
        
        c.set_a(10)
        c.set_b(100)
        result = c.sum()
        self.assertEqual(result, 110)
        self.assertIsInstance(result, int)
    
    def test_substract(self):
        c = Calculator(5, 6)
        result = c.substract()
        self.assertEqual(result, -1)
        self.assertIsInstance(result, int)
        
        c.set_a(100)
        c.set_b(10)
        result = c.substract()
        self.assertEqual(result, 90)
        self.assertIsInstance(result, int)
    
    def test_multiply(self):
        pass
    
    def test_divide(self):
        pass

if __name__ == "__main__":
    unittest.main()