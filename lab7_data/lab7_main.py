"""
hugo carcamo
lab 7, accessing data in a file
sep 29 2025
"""
from lab7_function import *

testing()
print("\n ---- example1: reading file ----")
with open('phrases.txt', 'r') as fileuser:
    eachline = fileuser.readlines()
    print(eachline)

email_read()