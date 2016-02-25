"""
Student: Max Sorto
Class: IT5090G - Aasheim
Date: 02/11/2016
Assignment: Lab4 - CH5
"""

# Declare variables to be used later on
count = 0
total = 0
largest = None
smallest = None

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
	
	# Compare the numbers
	if largest == None or number > largest:
		# Reassign new values to variable within the loop...
		largest = number		
		
	if smallest == None or number < smallest:
		# Reassign new values to variable within the loop...
		smallest = number
	
	# Reassign count and total variables	
	count += 1
	total += number
		
# Print the results
print total, count, largest, smallest
