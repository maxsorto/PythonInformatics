"""
Student: Max Sorto
Class: IT5090G - Aasheim
Date: 03/10/2016
Assignment: Lab8 - CH8
"""

# Import sys library to pass arguments at runtime...
import sys

# Pass the required files at runtime...
file_name = sys.argv[1]

# Open file
fhand = open(file_name)

# Initialize empty lines list and count variable...
lines = []
count = 0

# Print the file name to match the output in the exercise...
print "Enter a file name:", file_name

# Loop through lines in fhand...
for line in fhand:

	# If the lines starts with From, 
	# print the second item in the list and count it...
	if line.startswith("From"):
		words = line.split()
		count += 1
		print words[1]

# Print final count of emails...
print "There were", count, "lines in the file with From as the first word"