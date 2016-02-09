"""
Name: Max Sorto
Class: IT 5090G - Aasheim
Due: Feb. 3, 2016
Assignment: Project 2
"""

import sys

#Variables supplied by the user at runtime which will be used for BMI and Cholesterol calculations...
name = sys.argv[1]
height_input = sys.argv[2]
weight_input = sys.argv[3]
ldl_input = sys.argv[4]
hdl_input = sys.argv[5]
trig_input = sys.argv[6]

bmi = 0
cholesterol = 0


#Typecast inputs...
height_input = float(height_input)
weight_input = float(weight_input)
ldl_input = float(ldl_input)
hdl_input = float(hdl_input)
trig_input = float(trig_input)


#Function for calculating BMI
#Website used for NIH Guidelines on BMI levels: http://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmicalc.htm
def calc_bmi(height, weight) :

	bmi = (weight / height**2) * 703

	return bmi


print calc_bmi(height_input, weight_input)

#Function cholesterol...
def calc_chol(ldl, hdl, trig) :

	cholesterol = (hdl + ldl) + (trig / 5)
	
	return cholesterol


#Function for assigning BMI categories based on levels
def bmi_cat(bmi) :

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


#Function for assigning Cholesterol level categories
#Website used for NIH Guidelines on Cholesterol levels: http://www.nhlbi.nih.gov/health/resources/heart/heart-cholesterol-hbc-what-html
def chol_cat(cholesterol) :

	if cholesterol < 200:
		chol_label = 'desirable'
	elif cholesterol >= 200 and cholesterol <= 239:
		chol_label = 'borderline high'
	elif cholesterol >= 240:
		chol_label = 'high'
	else:
		chol_label = 'error'

	return chol_label


#Function for assigning LDL level categories
#Website used for NIH Guidelines on LDL levels: http://www.nhlbi.nih.gov/health/resources/heart/heart-cholesterol-hbc-what-html
def ldl_cat(ldl) :

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


#Function for assigning HDL level categories
#Website used for NIH Guidelines on HDL levels: https://www.nlm.nih.gov/medlineplus/magazine/issues/summer12/articles/summer12pg6-7.html
def hdl_cat(hdl) :

	if hdl < 40:
		hdl_label = 'a major risk factor for heart disease'
	elif hdl >= 40 and hdl <= 59:
		hdl_label = 'the higher, the better'
	elif hdl >= 60:
		hdl_label = 'considered protective against heart diseas'
	else:
		hdl_label = 'error'

	return hdl_label


#Function for assigning Triglyceride level categories
#Website used for NIH Guidelines on Triglyceride levels: https://www.nlm.nih.gov/medlineplus/ency/article/003493.htm
def tri_cat(trig) :

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


#Function to print statements to console displaying results for BMI and Cholesterol calculations...
def print_results() :

	b_result = calc_bmi(height_input, weight_input)
	ch = calc_chol(ldl_input, hdl_input, trig_input)
	b_cat = bmi_cat(bmi)
	ch_cat = chol_cat(ch)
	l_cat = ldl_cat(ldl_input)
	h_cat = hdl_cat(hdl_input)
	t_cat = tri_cat(trig_input)
	
	print 'Health status for',name+':'
	print ''
	print 'BMI:',b_result
	print 'Cholesterol:',ch
	print ''
	print 'BMI Category:',b_cat
	print 'Chol Category:',ch_cat
	print 'LDL Category:',l_cat 
	print 'HDL Category:',h_cat
	print 'Tri Category:',t_cat

#Call function that print results...
print_results()

