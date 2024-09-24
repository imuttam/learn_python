import sqlite3
from faker import Faker
import random

fakes = Faker('en_IN')

conn = sqlite3.connect('accounts.db')
cur = conn.cursor()


def create_table():
    conn.execute('''
              CREATE TABLE IF NOT EXISTS bank
               (id INTEGER PRIMARY KEY NOT NULL,
               name TEXT,
               balance REAL);
               ''')
    print('table created successfully')

def drop_table(table_name):
    conn.execute(f"DROP table {table_name}")
    print('table dropped successfully')

def add_user(name, balance):
    data = "INSERT INTO bank (name , balance) VALUES (?,?)"
    cur.execute(data,(name, balance))
    conn.commit()


def show_data():
    data = "SELECT * FROM bank"
    cur.execute(data)
    result = cur.fetchall()
    return result

def deposit(id, amount):
    cur.execute(f"UPDATE bank SET balance= balance+{amount}  WHERE id={id}")
    conn.commit()

def show_user(id):
    data = f"SELECT * FROM bank WHERE id = {id}"
    cur.execute(data)
    result = cur.fetchall()
    return result


def withdraw(id, amount):
    current_balance = show_user(id)[0][-1]
    if current_balance > amount:
        cur.execute(f"UPDATE bank SET balance= balance-{amount}  WHERE id={id}")
        conn.commit()
        return show_user(id)
    else:
        print(f"Sorry you don't have sufficient balance in your account.")


def delete_user(id):
    cur.execute(f"DELETE FROM bank WHERE id={id}")
    conn.commit()


"""add many user using loop """

def add_many(count):
    for i in range(count):
        name = fakes.first_name().lower()
        amount = random.randint(1000,5000)
        add_user(name, amount)


# create_table()
# add_user('pratham', 4134)

# deposit(1, 4000)
# print(show_data())
# print(show_user(1))
# withdraw(1, 200)
# print(show_user(1))

# delete_user(3)
print(show_data())

# drop_table('bank')

# add_many(50)