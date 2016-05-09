"""
Student: Max Sorto
Class: IT5090G - Aasheim
Date: 03/24/2016
Assignment: Lab12
"""

import pyodbc

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=IT3233BSQL2014\SQL41;DATABASE=sample;Trusted_Connection=yes')
cur = conn.cursor()

select = "SELECT * FROM employee"
query1 = "INSERT INTO employee VALUES (1001, 'Max', 'Sorto', NULL), (1002, 'Vincent', 'Lee', NULL)"
query2 = "SELECT project_no, COUNT(e.emp_no) as 'emps_on_proj' FROM employee e JOIN works_on w ON e.emp_no = w.emp_no GROUP BY project_no"
query3 = "SELECT emp_fname, emp_lname, project_name, job FROM employee e JOIN works_on w ON e.emp_no = w.emp_no JOIN project p ON w.project_no = p.project_no"
query4 = "SELECT emp_lname, COUNT(job) as 'num_jobs' FROM employee e JOIN works_on w ON e.emp_no = w.emp_no GROUP BY emp_lname"
query5 = "SELECT emp_lname, COUNT(job) as 'num_jobs' FROM employee e FULL OUTER JOIN works_on w ON e.emp_no = w.emp_no GROUP BY emp_lname"
query6 = "DELETE FROM employee WHERE emp_no IN (1001, 1002)"

cur.execute(query1)
cur.execute(select)

print 'Number 1:\n'
for row in cur:
	print row
print '\n'

cur.execute(query2)

print 'Number 2:\n'
for row in cur:
	print row
print '\n'

cur.execute(query3)
print 'Number 3:\n'

for row in cur:
	print row
print '\n'

cur.execute(query4)
print 'Number 4:\n'

for row in cur:
	print row
print '\n'

cur.execute(query5)
print 'Number 5:\n'

for row in cur:
	print row
print '\n'

cur.execute(query6)
cur.execute(select)
print 'Number 6:\n'

for row in cur:
	print row
print '\n'