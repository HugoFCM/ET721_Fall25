"""
hugo carcamo
lab 8, unittest
sep 29 2025
"""

import unittest
import calculations
from employee import Employee


# function to add and return sum of 2 numbers
def addtwonumbers(a, b):
    return a + b


# create a code to test function 'addtwonumbers'
class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(addtwonumbers(2, 3), 5)


class TestCalculation(unittest.TestCase):
    def test_multiplication(self):
        self.assertEqual(calculations.multiplythreenumbers(5), 5)
        self.assertEqual(calculations.multiplythreenumbers(2, 3), 6)
        self.assertEqual(calculations.multiplythreenumbers(2, 3, 4), 24)
        self.assertEqual(calculations.multiplythreenumbers(0), 0)


class TestEmployee(unittest.TestCase):
    # create a test template
    def setUp(self):
        # create an instant of a new employee
        self.emp1 = Employee("Peter", "Pen", 50000)

        # create a test for employee email

    def test_emailemployee(self):
        self.assertEqual(self.emp1.emailemployee, "Peter.Pan@email.com")

    # create a test for employee email
    def test_fullname(self):
        self.assertEqual(self.emp1.fullname, "Peter Pan")

        # update the first name
        self.emp1.first = "Will"

        # re-test full name
        self.assertEqual(self.emp1.fullname, "Will Pan")

    def test_salary(self):
        self.assertEqual(self.emp1.salary, 50000)

        self.emp1.apply_raise()

        self.assertEqual(self.emp1.salary, 52500)


if __name__ == "__main__":
    unittest.main()
