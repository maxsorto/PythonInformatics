"""
Name: Max Sorto
Class: IT 5090G - Aasheim
Due: Apr. 14, 2016
Exam 2
"""

lines = open('sales2.txt') # Read text file

sales = [] # Create empty list for sales

days_count = {} # Create empty dictionary

sales_total = {}

# Loop through sales and append the sale value to the list
for line in lines:

	try:
		
		content = line.split(' ')
		sale = content[2]
		sale = float(sale[1:])		
		day = content[1]

		# Count the number of instances of a day and add to days_count dictionary

		if day not in days_count:
			days_count[day] = 1
		else:
			days_count[day] += 1

		# Sum the total sales for each day of the week and add to sales_total dictionary

		if day not in sales_total:
			sales_total[day] = sale
		else:
			sales_total[day] += sale

	except:

		error_file = open('error.txt','w')
		error_file.write(str(line))
		error_file.close()
		continue

# Create output file
output = open('results2.txt', 'w') # Open file

line1 = 'Monday: $' + str(sales_total['Monday']/days_count['Monday']) + '\n'
line2 = 'Tueday: $' + str(sales_total['Tuesday']/days_count['Tuesday']) + '\n'
line3 = 'Wednesday: $' + str(sales_total['Wednesday']/days_count['Wednesday']) + '\n'
line4 = 'Thursday: $' + str(sales_total['Thursday']/days_count['Thursday']) + '\n'
line5 = 'Friday: $' + str(sales_total['Friday']/days_count['Friday']) + '\n'
line6 = 'Saturday: $' + str(sales_total['Saturday']/days_count['Saturday']) + '\n'
line7 = 'Sunday: $' + str(sales_total['Sunday']/days_count['Sunday']) + '\n'


# Write lines to file

output.write(line1)
output.write(line2)
output.write(line3)
output.write(line4)
output.write(line5)
output.write(line6)
output.write(line7)


output.close() # Close file
