"""
Hugo Carcamo
October 15th, 2025
Lab 10, File Operations
"""
import unittest
import os
from file_operations import read_file, write_file, append_file, email_read

class TestFileOperations(unittest.TestCase):
    def setUp(self):
        # set up temperary test file name before each test
        self.filename = "test_file.txt"
        self.msg = "Hugo Carcamo"

    def tearDown(self):
        # remove the test file after each test
        if os.path.exists(self.filename):
            os.remove(self.filename)
        
    def test_write_file(self):
        # test writing text to a file
        msg = "Hugo Carcamo"
        with open(self.filename, "w") as f:
            f.write(msg)

        # verify file exists and content matches
        self.assertTrue(os.path.exists(self.filename))
        with open(self.filename, "r") as f:
            result = f.read()
        
        self.assertEqual(result,msg)

    def test_read_file(self):
        # test reading text from a file
        expected_context = "Read me!"
        with open(self.filename, "w") as f:
            f.write(expected_context)
        
        with open(self.filename, "r") as f:
            data = f.read()

        self.assertEqual(data, expected_context)

    def test_append_file(self):
        # test appending text to an existing file
        initial_content = "Line one"
        append_content = "\nLine two"

        with open(self.filename,"w") as f:
            f.write(initial_content)

        with open(self.filename,"a") as f:
            f.write(append_content)

        with open(self.filename,"r") as f:
            final_data = f.read()
        
        self.assertEqual(final_data,(initial_content+append_content))

# LAB EXERCISE 
    def test_email_read(self):
        example_list = "test@gmail.com\ntest1@yahoo.com\ntest2@hotmail.com\ntest3@gmail.com"
        with open(self.filename, "w") as f:
            f.write(example_list)
        
        final_test = email_read(self.filename,"@gmail")        
        self.assertEqual(final_test, 2)
# run the unit test automatically when the file is run
if __name__ == "__main__":
    unittest.main()