"""
Student: Max Sorto
Class: IT5090G - Aasheim
Date: 01/28/2016
Assignment: Lab2 - CH3
"""

import sys

#Input required to be passed at runtime...
score = sys.argv[1]


#Try to typecast inputs to be able to do math,
#Otherwise if not numeric values then exit program...
try:
    score = float(score)
except:
	print 'Bad score - Enter a number between 0.0 and 1.0'
	sys.exit()

#Nested If/Else statement that first checks if score is between 0.0 and 1.0,
#Then assigns a grade letter depending on the score provided...
if 0.0 <= score <= 1.0:
	if score >= 0.9:
		grade = 'A'
	elif score >= 0.8 and score <= 0.89:
		grade = 'B'
	elif score >= 0.7 and score <= 0.79:
		grade = 'C'
	elif score >= 0.6 and score <= 0.69:
		grade = 'D'
	elif score < 0.6:
		grade = 'F'
	else:
		grade = 'Error - something went wrong'
else:
	grade = 'Bad score'

#Print statements to console...
print 'Enter Score:',score
print grade



