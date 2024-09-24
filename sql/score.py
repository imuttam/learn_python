import csv
import sqlite3

conn = sqlite3.connect('score.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        CardNo INTEGER,
        Name TEXT,
        Gender TEXT,
        DateOfBirth TEXT,
        CityTown TEXT,
        Mathematics INTEGER,
        Physics INTEGER,
        Chemistry INTEGER,
        Total INTEGER
    )
''')

# Read data from the CSV file and insert into the database
with open('./score.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip the header row

    for row in csvreader:
        # Convert string values to appropriate data types
        card_no, name, gender, dob, city, math, physics, chem, total = row
        card_no = int(card_no)
        math = int(math)
        physics = int(physics)
        chem = int(chem)
        total = int(total)


        # Insert data into the database
        cursor.execute('''
            INSERT INTO students (CardNo, Name, Gender, DateOfBirth, CityTown,
            Mathematics, Physics, Chemistry, Total)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (card_no, name, gender, dob, city, math, physics, chem, total))
