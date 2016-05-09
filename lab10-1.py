"""
Student: Max Sorto
Class: IT5090G - Aasheim
Date: 03/31/2016
Assignment: Lab10
"""

# Import necessary libraries...
import numpy as ny

# Data to be used...
data = "Joe 75,John 100,Mary 87,Lee 69"

# Split data into a list we can work with...
data = data.split(",")

# Create students a dictionary...
students = {}

# Create empty list for grades...
grades = []

for student in data:
	
	# Create indexes for finding grade and name...
	index = student.find(" ") + 1
	index2 = student.find(" ")

	# Set grade and name...
	grade = student[index:]
	name = student[:index2]

	# Typecast grade into int...
	grade = int(grade)

	# Populate students dictionary...
	students[name] = grade

	# Populate list of grades...
	grades.append(grade)

# Populate stats dictionary with calculations...

stats = {
	'std dev':  ny.std(grades),
	'max': ny.max(grades),
	'min': ny.min(grades),
	'mean': ny.mean(grades)
}
# Print stats dictionary...
print stats
