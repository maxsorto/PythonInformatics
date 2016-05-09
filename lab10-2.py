"""
Student: Max Sorto
Class: IT5090G - Aasheim
Date: 03/31/2016
Assignment: Lab10
"""

from pandas import DataFrame

data = {'name':['Joe','John','Mary','Lee'],
	'quiz 1':[100,87,99,78],
	'quiz 2':[45,78,90,88],
	'assign 1':[98,82,93,78],
	'assign 2':[100,87,99,78]
}

frame = DataFrame(data)
print frame
print '\n'
print frame.describe()