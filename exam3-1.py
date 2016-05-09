"""
Name: Max Sorto
Class: IT 5090G - Aasheim
Due: May. 3, 2016
Exam 3
"""

# Open the file to read from...
lines = open('data-student_grades1.csv')

next(lines) # Skip column labels

grades_count = {} # Create empty dictionary

my_file = open('results3-1.txt','w') # Create file to write output to

# Loop through lines and extract letter grade, then assign to dictionary
for line in lines:
	line = line.strip()
	content = line.split(',')
	grade = content[3]

	if grade not in grades_count:
		grades_count[grade] = 1
	else:
		grades_count[grade] += 1

key_order = ['W','I','A','B','C'] # Create a list with the order of desired output

# Write lines to file based on key_order...
for key in key_order:
	line = key + ': ' + str(grades_count[key]) + '\n'
	my_file.write(line)

# Close file...
my_file.close()

