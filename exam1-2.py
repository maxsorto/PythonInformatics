"""
---Exam 1---

Name: Max Sorto
Class: IT5090G - Aasheim
Date: 3/3/2016

File: exam1-2.py

---Exam 1---
"""

# Importing necessary library...
import sys

# Function that takes in a list of students and counts the number
# of male students

def count_males():

	count=0
	
	for student in sys.argv[1:]:
		
		gender = student.find(',') + 2
		
		if student[gender] == 'M':
			count += 1
	
	return count

# Function call to print results..	
print "Number of male students:",count_males()