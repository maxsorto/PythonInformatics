"""
Student: Max Sorto
Class: IT5090G - Aasheim
Date: 02/18/2016
Assignment: Lab5 - CH6
"""

import sys

# String that will be passed at runtime...
letter = sys.argv[1]
word = sys.argv[2]

# Defining count function that prints the count of a certain letter in a word...
def count(l, w):
	counter = 0
	for i in w:
		if i == l :
			counter = counter + 1
	return counter
		
# Encapsulate results of function call...
result = count(letter,word)

# Print results
print result