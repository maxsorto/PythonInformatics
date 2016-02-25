"""
Student: Max Sorto
Class: IT5090G - Aasheim
Date: 01/28/2016
Assignment: Lab2 - CH3
"""

import sys

#Input required to be passed at runtime...
hours = sys.argv[1]
rate = sys.argv[2]

#Try to typecast inputs to be able to do math with them, otherwise if not numeric values then exit program...
try:
    hours = float(hours)
    rate = float(rate)
except:
	print 'Error, please enter numeric input'
	sys.exit()

#Initialize other variables to be used in calculations...
pay = 0
overpay = 0
overtime = hours - 40

#If/Else to handle overtime pay...
if overtime > 0:
	overpay = overtime * (1.5 * rate)
	pay = 40 * rate
	pay += overpay
else:
	pay = hours * rate

#Print statements to console, converting hours and rate to int to match example's output...
print 'Enter Hours:',int(hours)
print 'Enter Rate:',int(rate)
print 'Pay:',pay



