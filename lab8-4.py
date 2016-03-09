"""
Student: Max Sorto
Class: IT5090G - Aasheim
Date: 03/10/2016
Assignment: Lab7 - CH8
"""

# Import sys library to pass arguments at runtime...
import sys

# Pass the required files at runtime...
file_name = sys.argv[1]

# Open file
fhand = open(file_name)

# Create empty word_list list...
word_list = []

# Begin for-loop to loop through lines in file...
for line in fhand:

	line = line.rstrip()	
	words = line.split(" ")

	# Begin another for-loop to loop through
	# the words in every line produced earlier...
	for word in words:

		# Add words to word_list that are not
		# already in there...
		if word not in word_list:
			word_list.append(word)

# Sort the word_list...
word_list.sort()

# Print the results...
print "Enter a file:", file_name
print word_list

