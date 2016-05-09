"""
Student: Max Sorto
Class: IT5090G - Aasheim
Date: 03/24/2016
Assignment: Lab9 - CH9
"""

import sys

file = sys.argv[1]

lines = open(file)

di_count = dict()

for line in lines:
	
	line = line.strip()
	
	word = line.split()
	
	if line.startswith("From "):
		di_count[word[2]] = di_count.get(word[2],0) + 1

print di_count
	