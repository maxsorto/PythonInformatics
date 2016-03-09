"""
Student: Max Sorto
Class: IT5090G - Aasheim
Date: 03/10/2016
Assignment: Lab8 - CH8
"""

# Initialize empty num_list list...
num_list = []

# While loop, executes when conditions are True and until
# the word "done" is typed into the terminal...
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
	
	# Add numbers entered by user to num_list...
	num_list.append(number)

# Print the min and max values of num_list...
print "Maximum:", max(num_list)
print "Minimum:", min(num_list)

