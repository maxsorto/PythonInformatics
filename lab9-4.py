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

limit = 0

email = None

for line in lines:

	line = line.strip()
	
	word = line.split()
	
	if line.startswith("From "):
		di_count[word[1]] = di_count.get(word[1],0) + 1
		
for user in di_count:
	
	if di_count[user] > limit:
	
		limit = di_count[user]
	
		email = user

print email, di_count[email]
	
	
