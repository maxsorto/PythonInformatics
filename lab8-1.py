"""
Student: Max Sorto
Class: IT5090G - Aasheim
Date: 03/10/2016
Assignment: Lab7 - CH8
"""

# Lists to be use for demo...

letters = ['a','b','c','x','y','z']

numbers = [1,2,3,4,5,6,7,8]

# Function that takes list and removes the first and last items,
# then returns None...
def chop(a_list):

	end = len(a_list) - 1 
	del a_list[end]
	del a_list[0]

	return None

# Function that returns everything in a list but the first and last item...
def middle(a_list):
	
	end = len(a_list) - 1

	return a_list[1:end]	

# Print list to demo functions...
print chop(letters)
print middle(numbers)