"""
The following code is given:

import sqlite3
conn = sqlite3.connect('northwind.db')
cur = conn.cursor()
cur.execute('''SELECT * FROM Category''')
rows = cur.fetchall()
for row in rows:
    print(row)
 
conn.close()


Modify the given query to display only the category name (second column) to the console (use a for loop).



Expected result:

Beverages
Condiments
Confections
Dairy Products
Grains/Cereals
Meat/Poultry
Produce
Seafood
"""

import sqlite3
conn = sqlite3.connect('northwind.db')
cur = conn.cursor()
cur.execute('''SELECT * FROM Category''')
rows = cur.fetchall()
for row in rows:
    print(row[1])
 
conn.close()