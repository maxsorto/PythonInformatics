"""
Student: Max Sorto
Class: IT5090G - Aasheim
Date: 02/04/2016
Assignment: Lab3 - CH4
"""

"""
Exercise 1 - In this program the imported random module contains a 
random function that prints a number between 0.0 and 1.0. 
Next, there is a loop that that iterates 10 times and prints a
value generated from random.random() 10 times. Running this
program produces new values in the range every time.

Exercise 2 - The error returned from moving a function call above
a function definition states that whatever function you have called
has not yet been defined: "NameError: name 'repeat_lyrics' is not defined"

Exercise 3 - The output from moving the second function definition before
the first one is the same as if the functions had not been moved.
When a function is called it will look for its definition in the program
and jump to that position, then if that function has another function call
in its definition, Python will look for the definition wherever it is in
the program.

Exercise 4 - D. The purpose of the 'def' keyword in Python is to indicate the
start of a function and indicate that the following indented section of code
is to be stored for later.

Exercise 5 - D. The output of this program is: 
ABC 
Zap 
ABC
"""

#Start of Exercise 6...

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

#Definition for computepay function...
def computepay(hours, rate):
	
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
	
computepay(hours,rate)
