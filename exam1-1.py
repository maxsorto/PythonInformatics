"""
---Exam 1---

Name: Max Sorto
Class: IT5090G - Aasheim
Date: 3/3/2016

File: exam1-1.py

---Exam 1---
"""

# Importing necessary library...
import sys

# Capturing values that are passed at runtime...
sysname = sys.argv[1]
sysage = sys.argv[2]

# Function that takes the name and frequency of visits of a customer 
# at X shop and returns a message depending on the frequency...
def frequent_cust(name, freq):
	
	try:
		freq = float(freq)
	except:
		print "Error: did not enter number for visit frequency average"
		sys.exit()
	
	if freq > 0 and freq < 1.0:
		message = "capricious customer"
	elif freq > 1.0 and freq < 4.0:
		message = "regular customer"
	elif freq >= 4.0:
		message = "very frequent customer"
	else:
		message = "capricious customer"
		
	return name + " is a " + message
	
# Print the function call to frequent_cust using the supplied variables..
print frequent_cust(sysname,sysage)