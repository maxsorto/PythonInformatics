"""
Student: Max Sorto
Class: IT5090G - Aasheim
Date: 02/25/2016
Assignment: Lab6 - CH7
"""

import sys

# Pass file path variable at runtime...
fpath = sys.argv[1]

# Open the file...
fhand = open(fpath)

# Loop through every line in the file, capitalize every character,
# strip the extra line, the print every line...
for line in fhand:
	line = line.rstrip()
	print line.upper()
