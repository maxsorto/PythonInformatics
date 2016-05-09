"""
Name: Max Sorto
Class: IT 5090G - Aasheim
Due: May. 3, 2016
Exam 3
"""

# Open the file to read from...
lines = open('data-student_grades1.csv')

my_file = open('results3-2.txt','w') # Create file to write output to

# Create a variable with the labels to print to results3-2.txt file...
labels = lines.readline().strip()

my_file.write(labels + ',Numeric_Grade' + '\n') # Write labels to first line of file


# Define function calc_grade that assigns a numeric value to a letter grade passed to it...
def calc_grade(grade):
	if grade == 'A':
		num_g = 4.0
	elif grade == 'B':
		num_g = 3.0
	elif grade == 'C':
		num_g = 2.0
	elif grade == 'D':
		num_g = 1.0
	else:
		num_g = 'N/A'

	return num_g


# Loop through lines to extract letter grade then run the calc_grade function on it...
for line in lines:
	line = line.strip()
	content = line.split(',')
	grade = content[3]
	num_grade = calc_grade(grade)
	new_line = line + ',' + str(num_grade) + '\n'

	my_file.write(new_line)  # Write new line with numeric grade to results file.

# Close file...
my_file.close()


