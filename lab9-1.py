"""
Student: Max Sorto
Class: IT5090G - Aasheim
Date: 03/24/2016
Assignment: Lab9 - CH9
"""

file = open('words.txt')

word = dict()

for lines in file:

	lines = lines.rstrip()
	
	line = lines.split()
	
	for line in lines:
		word[line] = 'Value'
		
print word

		
