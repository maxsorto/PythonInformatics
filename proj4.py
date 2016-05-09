"""
patient_id: Max Sorto
Class: IT 5090G - Aasheim
Due: Mar. 24, 2016
Assignment: Project 4
"""

import sys

# Function that finds data in a long string based on a set start and end,
# then returns just the number found...
def get_data(search_term,a_string):
	
	parameter = search_term
	index = a_string.find(parameter) + len(parameter)
	end = a_string.find(',', index)
	number = a_string[index:end]

	return number


# Define a function that returns a value of -1 for non-int values,
# or returns the typecasted number...
def get_ints(an_int):
		
	if int(an_int) == False:
		return '-1'
	else:
		new_int = int(an_int)
		return new_int


# Function for calculating BMI
# Website used for NIH Guidelines on BMI levels: http://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmicalc.htm
def calc_bmi(height, weight):

	weight = float(weight)
	height = float(height)

	bmi = (weight / height**2) * 703

	return bmi

# Function cholesterol...
def calc_chol(ldl, hdl, trig):

	hdl = float(hdl)
	ldl = float(ldl)
	trig = float(trig)

	cholesterol = (hdl + ldl) + (trig / 5)

	return cholesterol


# Function for assigning BMI categories based on levels
def bmi_cat(bmi):

	bmi = calc_bmi(height_input, weight_input)

	if bmi < 18.5:
		bmi_label = 'underweight'
	elif bmi >= 18.5 and bmi <= 24.9:
		bmi_label = 'normal weight'
	elif bmi >= 25 and bmi <= 29.9:
		bmi_label = 'normal weight'
	elif bmi >= 30:
		bmi_label = 'obesity'
	else:
		bmi_label = 'error'

	return bmi_label


# Function for assigning Cholesterol level categories
# Website used for NIH Guidelines on Cholesterol levels: http://www.nhlbi.nih.gov/health/resources/heart/heart-cholesterol-hbc-what-html
def chol_cat(cholesterol):

	if cholesterol < 200:
		chol_label = 'desirable'
	elif cholesterol >= 200 and cholesterol <= 239:
		chol_label = 'borderline high'
	elif cholesterol >= 240:
		chol_label = 'high'
	else:
		chol_label = 'error'

	return chol_label


# Function for assigning LDL level categories
# Website used for NIH Guidelines on LDL levels: http://www.nhlbi.nih.gov/health/resources/heart/heart-cholesterol-hbc-what-html
def ldl_cat(ldl):

	if ldl < 100:
		ldl_label = 'optimal'
	elif ldl >= 100 and ldl <= 129:
		ldl_label = 'near optimal'
	elif ldl >= 130 and ldl <= 159:
		ldl_label = 'borderline high'	
	elif ldl >= 160 and ldl <= 189:
		ldl_label = 'high'
	elif ldl >= 190:
		ldl_label = 'very high'
	else:
		ldl_label = 'error'

	return ldl_label


# Function for assigning HDL level categories
# Website used for NIH Guidelines on HDL levels: https://www.nlm.nih.gov/medlineplus/magazine/issues/summer12/articles/summer12pg6-7.html
def hdl_cat(hdl):

	if hdl < 40:
		hdl_label = 'a major risk factor for heart disease'
	elif hdl >= 40 and hdl <= 59:
		hdl_label = 'the higher the better'
	elif hdl >= 60:
		hdl_label = 'considered protective against heart diseas'
	else:
		hdl_label = 'error'

	return hdl_label


# Function for assigning Triglyceride level categories
# Website used for NIH Guidelines on Triglyceride levels: https://www.nlm.nih.gov/medlineplus/ency/article/003493.htm
def tri_cat(trig):

	if trig < 150:
		trig_label = 'normal'
	elif trig >= 150 and trig <= 199:
		trig_label = 'borderline high'
	elif trig >= 200 and trig <= 499:
		trig_label = 'high'
	elif trig >= 500:
		trig_label = 'very high'
	else:
		trig_label = 'error'

	return trig_label


# Function to print results to output.txt file
def print_results():

	b_result = calc_bmi(height_input, weight_input)
	ch = calc_chol(ldl_input, hdl_input, trig_input)
	b_cat = bmi_cat(bmi)
	ch_cat = chol_cat(ch)
	l_cat = ldl_cat(ldl_input)
	h_cat = hdl_cat(hdl_input)
	t_cat = tri_cat(trig_input)
	
	file = open('output.txt', 'a') # Open file

	line1 = 'Patient ' + patient_id + ':\n'
	line2 = 'BMI: ' + str(b_result)
	line3 = 'BMI Category: ' + str(b_cat) + '\n'	
	line4 = 'Total Chol: ' + str(ch)
	line5 = 'Chol Cat: ' + str(ch_cat) + '\n'
	line6 = 'LDL Cat: ' + str(l_cat) 
	line7 = 'HDL Cat ' + str(h_cat)
	line8 = 'Triglyc Cat: ' + str(t_cat) + '\n\n'

	# Write lines to file

	file.write(line1)
	file.write(line2)
	file.write(line3)
	file.write(line4)
	file.write(line5)
	file.write(line6)
	file.write(line7)
	file.write(line8)

	file.close() # Close file
	

# Initialize bmi and cholesterol global variables...
bmi = 0
cholesterol = 0

# Open data.csv file
lines = open('data.csv')

next(lines) # Skips line with column headers in .csv

for line in lines:
	line = line.rstrip() # Remove blank lines

	# Define variables extracted from line...
	patient_id = get_data('',line)
	height_input = get_data('ht:',line)
	weight_input = get_data('wt:',line)
	ldl_input = get_data('ldl:',line)
	hdl_input = get_data('hdl:',line)
	trig_input = get_data('tri:',line)

	try:		
		# Try to typecast inputs...
		height_input = get_ints(height_input)
		weight_input = get_ints(weight_input)
		ldl_input = get_ints(ldl_input)
		hdl_input = get_ints(hdl_input)
		trig_input = get_ints(trig_input)

		# Call function that prints results...
		print_results()

	except: 
		# If data provided is not an int, then write line to error.txt...
		errorfile = open('error.txt', 'a')
		errorfile.write(line + '\n\n')
		errorfile.close()
