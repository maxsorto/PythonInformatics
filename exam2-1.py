"""
Name: Max Sorto
Class: IT 5090G - Aasheim
Due: Apr. 14, 2016
Exam 2
"""

lines = open('sales1.txt') # Read text file

sales = [] # Create empty list for sales

# Loop through sales and append the sale value to the list
for line in lines: 
	line = line.split(' ')
	sale = line[2]
	sale = float(sale[1:])
	sales.append(sale)

# Find max, min and avg using built in functions
find_max = max(sales)
find_min = min(sales)
find_avg = sum(sales)/len(sales)
 
# Create output file
output = open('results1.txt', 'w') # Open file

line1 = 'Max: $' + str(find_max) + '\n'
line2 = 'Min: $' + str(find_min) + '\n'
line3 = 'Avg: $' + str(find_avg) + '\n'

# Write lines to file

output.write(line1)
output.write(line2)
output.write(line3)

output.close() # Close file
