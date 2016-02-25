"""
Student: Max Sorto
Class: IT5090G - Aasheim
Date: 02/18/2016
Assignment: Lab5 - CH6
"""

import sys

# String that will be passed at runtime...
fruit = sys.argv[1]

# Set index of word at the end of the string, minus one character...
index = len(fruit) - 1

# While the index is greater than or equal to zero, set letter to the index of fruit,
# then, print the letter at that index,
# then reduce the index by 1 until it reaches 0 to exit the loop...
while index >= 0:
	letter = fruit[index]
	print letter
	index = index - 1
