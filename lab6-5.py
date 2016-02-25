"""
Student: Max Sorto
Class: IT5090G - Aasheim
Date: 02/18/2016
Assignment: Lab5 - CH6
"""

import sys

# String that will be passed at runtime...
str = sys.argv[1]

# Find the index of where the number in the string is...
index = str.find(':') + 1

# Create the slice of string that has numbers...
slice = str[index:]

# Convert slice to float...
slice = float(slice)

# Print the slice
print slice