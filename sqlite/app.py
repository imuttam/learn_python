import sqlite3
from faker import Faker
from datetime import datetime
import pandas as pd 

# Initialize Faker for Indian locale
faker = Faker('en_IN')

# Function to create the 'Students' table
def create_table():
    with sqlite3.connect('students.db') as connection:
        cursor = connection.cursor()
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS Students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            city TEXT,
            email TEXT
        );
        '''
        cursor.execute(create_table_query)
        connection.commit()
        print("Table 'Students' created successfully!")

# Function to generate fake student data
def create_data():
    # Generate name, date, city, and email
    name = faker.name()
    birthdate = faker.date_of_birth(minimum_age=18, maximum_age=40)  # Generates realistic age
    age = datetime.now().year - birthdate.year
    city = faker.city()
    email = faker.email()

    # Format the date in 'dd-mm-yy' format
    formatted_birthdate = birthdate.strftime('%d-%m-%y')

    # Print and return the data
    data = (name, age, city, email)
    print(data)
    return data

# Function to insert generated data into the 'Students' table
def insert_data(data):
    with sqlite3.connect('students.db') as connection:
        cursor = connection.cursor()
        insert_query = '''
        INSERT INTO Students (name, age, city, email) 
        VALUES (?, ?, ?, ?);
        '''
        cursor.execute(insert_query, data)
        connection.commit()
        print("Record inserted successfully!")

def view_data():
    with sqlite3.connect('students.db') as connection:
        cursor = connection.cursor()

        # Execute a SELECT query to fetch data from the Students table
        cursor.execute("SELECT * FROM Students")
        records = cursor.fetchall()
        return records
    

def show_data():

    with sqlite3.connect('students.db') as connection:
        # Load the data directly into a pandas DataFrame
        df = pd.read_sql_query("SELECT * FROM Students", connection)
        return df




# Create table if it doesn't exist
# create_table()

# Insert 5 records
# for _ in range(95):
#     insert_data(create_data())

# Retrieve the records and print them
# records = view_data()
# for record in records:
#     print(record)


# Call the function and display the data
student_df = show_data()
# print(student_df.head(20))

filtered_age = student_df[student_df['age']>30]
filtered_age = filtered_age.columns[]
print(filtered_age)