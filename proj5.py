"""
Name: Max Sorto
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

# Function for assigning Systolic Blood Pressure level categories
# Website used for NIH Guidelines on Systolic Blood Pressure levels: http://www.webmd.com/hypertension-high-blood-pressure/guide/diastolic-and-systolic-blood-pressure-know-your-numbers
def syscat(systolic):

	if systolic < 120:
		sys_label = 'normal'
	elif systolic >= 120 and systolic <= 139:
		sys_label = 'prehypertension'
	elif systolic >= 140:
		sys_label = 'hypertension'
	else:
		sys_label = 'error'

	return sys_label

# Function for assigning Diastolic Blood Pressure level categories
# Website used for NIH Guidelines on Diastolic Blood Pressure levels: http://www.webmd.com/hypertension-high-blood-pressure/guide/diastolic-and-systolic-blood-pressure-know-your-numbers
def diacat(diastolic):

	if diastolic < 80:
		dia_label = 'normal'
	elif diastolic >= 80 and diastolic <= 89:
		dia_label = 'prehypertension'
	elif diastolic >= 90:
		dia_label = 'hypertension'
	else:
		dia_label = 'error'

	return dia_label

# Function to check if gender supplies is valid...

def gen_check(gen):

	if gen == 'M':
		gen = 'M'
	elif gen == 'F':
		gen = 'F'
	else:
		sys.exit()

	return gen

# Function that finds 'Notes' in a string...
def get_notes(a_string):
	
	split = a_string.split(',')
	note = split[-1]

	return note

# Create lists for BMI, LDL, Cholesterol, Blood Pressure...

gendata = []
bmidata = []
choldata = []
bpdata = []

# Function to assign results to their respective variables and lists...
def assign_results():

	b_result = calc_bmi(height_input, weight_input)
	ch = calc_chol(ldl_input, hdl_input, trig_input)
	b_cat = bmi_cat(bmi)
	ch_cat = chol_cat(ch)
	l_cat = ldl_cat(ldl_input)
	h_cat = hdl_cat(hdl_input)
	t_cat = tri_cat(trig_input)
	s_cat = syscat(sys_input)
	d_cat = diacat(dia_input)

	# Populate lists with lists...
	gendata.append([patient_id, gen_input])
	bmidata.append([patient_id, b_result, height_input, weight_input, b_cat])
	choldata.append([patient_id, ch, ch_cat, ldl_input, l_cat, hdl_input, h_cat])
	bpdata.append([patient_id, sys_input, s_cat, dia_input, d_cat])

	file = open('output.txt', 'a') # Open file

	line1 = 'Patient ' + patient_id + ' - Gender: ' + gen_input + '\n'
	line2 = 'BMI: ' + str(b_result) + '\t' + 'BMI Category: ' + str(b_cat) + '\n'
	line3 = 'Total Chol: ' + str(ch) + '\t' + 'Chol Cat: ' + str(ch_cat) + '\n'
	line4 = 'LDL Cat: ' + str(l_cat) + '\t' + 'HDL Cat ' + str(h_cat) + '\t' + 'Triglyc Cat: ' + str(t_cat) + '\n'
	line5 = 'Systolic BP: ' + str(sys_input) + '\t' + 'Systolic Cat ' + s_cat + '\n'
	line6 = 'Diastolic BP: ' + str(dia_input) + '\t' + 'Diastolic Cat ' + d_cat
	line7 = note_input + '\n\n'

	# # Write lines to file

	file.write(line1)
	file.write(line2)
	file.write(line3)
	file.write(line4)
	file.write(line5)
	file.write(line6)
	file.write(line7)

	file.close() # Close file


# Function that takes a list and prints it formatted to 'output.txt'...
def print_list(a_list):

	file = open('output.txt', 'a') # Open file

	for item in a_list:
		file.write('%s\n' % item)

	file.write('\n')
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
	sys_input = get_data('sys:',line)
	dia_input = get_data('dia:',line)
	gen_input = get_data('gen:',line)
	note_input = get_notes(line)

	try:		

		gen_check(gen_input)
		# Try to typecast inputs...
		height_input = get_ints(height_input)
		weight_input = get_ints(weight_input)
		ldl_input = get_ints(ldl_input)		
		hdl_input = get_ints(hdl_input)
		trig_input = get_ints(trig_input)
		sys_input = get_ints(sys_input)
		dia_input = get_ints(dia_input)


		# Call function that assign results...
		assign_results()

	except: 
		# If data provided is not an int, then write line to error.txt...
		errorfile = open('error.txt', 'a')
		errorfile.write(line + '\n\n')
		errorfile.close()

# Call print lists function to add data from lists to 'output.txt'...
print_list(gendata)
print_list(bmidata)
print_list(choldata)
print_list(bpdata)

