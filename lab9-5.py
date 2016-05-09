"""
Student: Max Sorto
Class: IT5090G - Aasheim
Date: 03/24/2016
Assignment: Lab9 - CH9
"""

import sys

file = sys.argv[1]

lines = open(file)

lines = [line.strip('\n') for line in open(file)
         if line.startswith("From ")]

new_dict = {}

for line in lines:

    line = line.split()
    
    email = line[1]
    
    mail_slice = email.split("@")[1]
    
    new_dict[mail_slice] = new_dict.get(mail_slice, 0) + 1

print new_dict