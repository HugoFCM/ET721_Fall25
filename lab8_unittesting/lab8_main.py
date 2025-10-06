"""
hugo carcamo
lab 8, unittest
sep 29 2025
"""

import unittest
import calculations

# function to add and return sum of 2 numbers
def addtwonumbers(a,b):
    return a+b

# create a code to test function 'addtwonumbers'
class TestAddFunction(unittest.TestCase):
    def test_add(self):
                 self.assertEqual(addtwonumbers(2,3),5)
class TestCalculation(unittest.TestCase):
       def test_multiplication(self):
              self.assertEqual(calculations.multiplythreenumbers(5), 5)
              self.assertEqual(calculations.multiplythreenumbers(2,3), 6)
              self.assertEqual(calculations.multiplythreenumbers(2,3, 4), 24)
              self.assertEqual(calculations.multiplythreenumbers(0), 0)

if __name__ =="__main__":
       unittest.main()