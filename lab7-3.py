"""
Student: Max Sorto
Class: IT5090G - Aasheim
Date: 02/25/2016
Assignment: Lab6 - CH7
"""

import sys

# Pass file path variable at runtime...
fname = sys.argv[1]

# Easter egg if file path matches...
if fname == 'na na boo boo':
	print "NA NA BOO BOO TO YOU - You have been punk'd!"
	sys.exit()

# try/except block for opening valid file names...
try:
	fhand = open(fname)
except:
	print 'File cannot be opened:', fname
	sys.exit()

# Set counter...
count = 0

# Loop through each line and count the lines starting with "Subject:"...
for line in fhand:
	if line.startswith('Subject:') :
		count = count + 1
		
# Print line count for valid files...
print 'There were', count, 'subject lines in', fname