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

# Set a counter and variable for the sum of all numbers...
count = 0
sum = 0

# Loop through every line in the file,
# then if the line starts with the specified pattern,
# set the starting index to the placement of a colon plus 2 spaces,
# next, slice from the index until the end of the line to find floats,
# then cast to a float,
# finally, count lines and sum up all averages...
for line in fhand:
		
	if line.startswith('X-DSPAM-Confidence:'):
		start = line.find(":") + 2

		flt = line[start:]
		flt = float(flt)
		
		count += 1
		sum += flt

# Finally print a message and the average...
print "Average spam confidence:", (sum/count)
