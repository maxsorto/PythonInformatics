"""
Student: Max Sorto
Class: IT5090G - Aasheim
Date: 02/11/2016
Assignment: Lab4 - CH5
"""

# Declare variables to be used later on
count = 0
total = 0
average = 0

# While loop, executes when conditions are True and until 
while True:
	
	number = raw_input('Enter a number: ')
	
	if number == 'done':
		break
		
	# Try to typecast inputs to be able to do math,
	# Otherwise if not numeric values then exit program...
	try:
		number = float(number)
	except:
		print 'Invalid input'
		continue
	
	# Reassign new values to variable within the loop...
	count += 1
	total += number
	average = total/count
	
# Print the results
print total, count, average
