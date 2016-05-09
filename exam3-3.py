"""
Name: Max Sorto
Class: IT 5090G - Aasheim
Due: May. 3, 2016
Exam 3
"""

# Open the file to read from...
lines = open('data-student_grades2.csv')

next(lines) # Skip first line to exclude column labels

my_file = open('results3-3.txt','w') # Create file to write output to

grades_count = {} # Create empty dictionary

grades_total = {} # Create empty dictionary

# Loop through lines and extract numeric grade, then assign to dictionary
# Populate dictionaries to hold counts and totals for grades by prof_id
for line in lines:
	line = line.strip()
	content = line.split(',')
	num_grade = content[4]

	if num_grade == 'N/A':
		continue
	else:
		num_grade = float(num_grade)

	prof_id = content[1]

	if prof_id not in grades_count:
		grades_count[prof_id] = 1
	else:
		grades_count[prof_id] += 1


	if prof_id not in grades_total:
		grades_total[prof_id] = num_grade
	else:
		grades_total[prof_id] += num_grade

key_order = ['1','3','5','6','7','8','10','11','12','17','19'] # Create a list with the order of desired output

for key in key_order:
	new_line = key + ': ' + str(grades_total[key]/grades_count[key]) + '\n'
	my_file.write(new_line)

# Close file...
my_file.close()


