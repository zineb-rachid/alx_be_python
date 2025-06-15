import unittest
from simple_calculator import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
           #set up the SimpleCalculator instance before each test."""
        self.calc=SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2,4),6)
        self.assertEqual(self.calc.add(2,18),20)
    def test_division(self):
        self.assertEqual(self.calc.divide(1,0),None)
        self.assertEqual(self.calc.divide(4,2),2)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3,2),6)
        self.assertEqual(self.calc.multiply(1,0),0)
    def test_test_subtraction(self):
        self.assertEqual(self.calc.subtract(4,6),-2)
        self.assertEqual(self.calc.subtract(5,2),3)
if __name__ == "__main__" :
    unittest.main()
    
    

