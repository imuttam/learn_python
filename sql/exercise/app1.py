import sqlite3

with sqlite3.connect('northwind.db') as conn:
    cur = conn.cursor()
    # To get the all table details on database
    # query = "SELECT name FROM sqlite_master WHERE type='table';"
    query = "SELECT * FROM Category"
    res = cur.execute(query)
    row1 = res.fetchone()
    row2 = res.fetchone()

"""
Ques1: Using the sqlite3 package connect to the northwind.db database. Then create a Cursor object and execute the following SQL query to the database:
SELECT * FROM Category
Using the appropriate method, print the first row from the above query to the console. Finally, close the database connection.

Expected result:
(1, 'Beverages', 'Soft drinks, coffees, teas, beers, and ales')
"""
# Answer1 
# print(row)

"""
Using the Cursor.fetchone() method, assign the first two rows of the above query to the variables:
Display the contents of the variables 
first_row and second_row to the console as shown below and close the database connection.
"""
print(row1)
print(row2)