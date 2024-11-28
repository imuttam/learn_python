"""
Using the sqlite3 package connect to the northwind.db database. Then create a Cursor object and execute the SQL query that returns the following columns:

FirstName

LastName

Title

City

from the Employee table.

Using a for loop, display each row returned by the created query to the console as shown below.
Expected result:

('Nancy', 'Davolio', 'Sales Representative', 'Seattle')
('Andrew', 'Fuller', 'Vice President, Sales', 'Tacoma')
('Janet', 'Leverling', 'Sales Representative', 'Kirkland')
('Margaret', 'Peacock', 'Sales Representative', 'Redmond')
('Steven', 'Buchanan', 'Sales Manager', 'London')
('Michael', 'Suyama', 'Sales Representative', 'London')
('Robert', 'King', 'Sales Representative', 'London')
('Laura', 'Callahan', 'Inside Sales Coordinator', 'Seattle')
('Anne', 'Dodsworth', 'Sales Representative', 'London')

"""

import sqlite3

with sqlite3.connect('northwind.db') as conn:
    cur = conn.cursor()
    query = "SELECT * FROM Employee"
    res = cur.execute(query)
    rows = res.fetchall()

for row in rows:
    print(row[0],row[2],row[1],row[3],row[8])
