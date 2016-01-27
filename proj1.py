"""
Name: Max Sorto
Class: IT 5090G - Aasheim
Due: Jan. 28, 2016
Assignment: Project 1
"""

import sys

#Variables supplied by the user at runtime which will be used for BMI and Cholesterol calculations...
name = sys.argv[1]
height = sys.argv[2]
weight = sys.argv[3]
ldl = sys.argv[4]
hdl = sys.argv[5]
trig = sys.argv[6]

#Typecast inputs...
height = float(height)
weight = float(weight)
ldl = float(ldl)
hdl = float(hdl)
trig = float(trig)

#Formulas for bmi and cholesterol...
bmi = (weight / height**2) * 703
cholesterol = (hdl + ldl) + (trig / 5)

#If/Else for BMI level categories
#Website used for NIH Guidelines on BMI levels: http://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmicalc.htm
if bmi < 18.5:
	bmi_category = 'underweight'
elif bmi >= 18.5 and bmi <= 24.9:
	bmi_category = 'normal weight'
elif bmi >= 25 and bmi <= 29.9:
	bmi_category = 'normal weight'
elif bmi >= 30:
	bmi_category = 'obesity'
else:
	bmi_category = 'error'

#If/Else for Cholesterol level categories
#Website used for NIH Guidelines on Cholesterol levels: http://www.nhlbi.nih.gov/health/resources/heart/heart-cholesterol-hbc-what-html
if cholesterol < 200:
	chol_category = 'desirable'
elif cholesterol >= 200 and cholesterol <= 239:
	chol_category = 'borderline high'
elif cholesterol >= 240:
	chol_category = 'high'
else:
	chol_category = 'error'

#If/Else for LDL level categories
#Website used for NIH Guidelines on LDL levels: http://www.nhlbi.nih.gov/health/resources/heart/heart-cholesterol-hbc-what-html
if ldl < 100:
	ldl_category = 'optimal'
elif ldl >= 100 and ldl <= 129:
	ldl_category = 'near optimal'
elif ldl >= 130 and ldl <= 159:
	ldl_category = 'borderline high'	
elif ldl >= 160 and ldl <= 189:
	ldl_category = 'high'
elif ldl >= 190:
	ldl_category = 'very high'
else:
	ldl_category = 'error'

#If/Else for HDL level categories
#Website used for NIH Guidelines on HDL levels: https://www.nlm.nih.gov/medlineplus/magazine/issues/summer12/articles/summer12pg6-7.html
if hdl < 40:
	hdl_category = 'a major risk factor for heart disease'
elif hdl >= 40 and hdl <= 59:
	hdl_category = 'the higher, the better'
elif hdl >= 60:
	hdl_category = 'considered protective against heart diseas'
else:
	hdl_category = 'error'

#If/Else for Triglyceride level categories
#Website used for NIH Guidelines on Triglyceride levels: https://www.nlm.nih.gov/medlineplus/ency/article/003493.htm
if trig < 150:
	trig_category = 'normal'
elif trig >= 150 and trig <= 199:
	trig_category = 'borderline high'
elif trig >= 200 and trig <= 499:
	trig_category = 'high'
elif trig >= 500:
	trig_category = 'very high'
else:
	trig_category = 'error'

#Print statements to console displaying results for BMI and Cholesterol calculations...
print 'Health status for',name
print ''
print 'BMI:',bmi
print 'Cholesterol:',cholesterol
print ''
print 'BMI Category:',bmi_category
print 'Chol Category:',chol_category
print 'LDL Category:',ldl_category 
print 'HDL Category:',hdl_category
print 'Tri Category:',trig_category

