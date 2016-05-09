"""
Student: Max Sorto
Class: IT5090G - Aasheim
Date: 03/24/2016
Assignment: Lab12
"""

import pandas as pd
import matplotlib.pyplot as plt
import pyodbc

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=IT3233BSQL2014\SQL41;DATABASE=studentgrades;Trusted_Connection=yes')
cur = conn.cursor()

query = "SELECT Period_ID, cs.Section_Number, cs.Course_ID, cs.Course_Name, Student_ID, p.Prof_ID, p.Prof_Name, cg.Course_Grade, cg.Numeric_Grade FROM Course_Grade cg JOIN Course_Section cs ON cg.Section_Number = cs.Section_Number JOIN Professor p ON cg.Prof_ID = p.Prof_ID"
query2 = "SELECT cs.Course_ID, p.Prof_ID, cg.Numeric_Grade FROM Course_Grade cg JOIN Course_Section cs ON cg.Section_Number = cs.Section_Number JOIN Professor p ON cg.Prof_ID = p.Prof_ID"

df = pd.read_sql(query, conn)
df2 = pd.read_sql(query2, conn)

a = pd.value_counts(df['Course_Grade'])
b = df['Numeric_Grade'].groupby(df['Prof_ID']).mean()
c = df2.groupby(['Prof_ID','Course_ID']).mean()
d = df['Course_Grade'].groupby(df['Prof_ID']).size()
e = df['Course_Grade'].groupby(df['Prof_ID']).value_counts()

# Plot graphs to figure, then subplots into figure...

plt.figure(1)
plt.subplot(131)
a.plot.bar()

plt.subplot(132)
b.plot.bar()

plt.subplot(133)
d.plot.bar()

plt.show()
