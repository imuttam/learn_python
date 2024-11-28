"""
Using the sqlite3 package connect to the northwind.db database. Then create a Cursor object and execute the SQL query that returns the following columns:

FirstName

LastName

Title

City

from the Employee table.
Using the Cursor.fetchmany() method, retrieve the first three rows returned by the created query. In response, use a for loop to display each of these rows to the console as shown below.
Expected result:

('Nancy', 'Davolio', 'Sales Representative', 'Seattle')
('Andrew', 'Fuller', 'Vice President, Sales', 'Tacoma')
('Janet', 'Leverling', 'Sales Representative', 'Kirkland')
"""

import sqlite3

with sqlite3.connect('northwind.db') as conn:
    cur = conn.cursor()
    query = "SELECT * FROM Employee limit 3"
    res = cur.execute(query)
    rows = res.fetchall()

for row in rows:
    print(row)