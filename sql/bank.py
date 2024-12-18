import sqlite3
from faker import Faker
import random

fakes = Faker('en_IN')

conn = sqlite3.connect('accounts.db')
cur = conn.cursor()

# print('database created successfully!')

# conn.execute('''
#               CREATE TABLE IF NOT EXISTS account
#                (id INTEGER PRIMARY KEY NOT NULL,
#                name TEXT,
#                balance REAL);
#                ''')

"""Single insertion....."""

# cur.execute("""
#     INSERT INTO account (name, balance) VALUES
#         ('kanchan', 2000),
#         ('advait', 3000)
# """)

########################################################

"""Many Insertion """

# data = []
# for i in range(39):
#     name = fakes.name()
#     num = random.randint(1000,5000)
#     data.append((name, num))

# cur.executemany("INSERT INTO account VALUES(NULL, ?, ?)", data)
# conn.commit()

##########################################################

# res = cur.execute("SELECT name FROM sqlite_master")
# print(res.fetchone())

"""Using Function"""

def create_data():
    data = []
    for i in range(39):
        name = fakes.name()
        num = random.randint(1000,5000)
        data.append((name, num))
    return data

def register(name, balance):
    cur.execute('INSERT INTO account VALUES (NULL,?,?)', (name,balance))
    conn.commit()

def register_many():
    # cur.executemany("INSERT INTO account VALUES(NULL, ?, ?)", data)
    data = create_data()
    for item in data:
        cur.execute('INSERT INTO account VALUES (NULL,?,?)', item)
        conn.commit()

def deposit(amount, id):
    cur.execute(f"UPDATE account SET balance= balance+{amount}  WHERE id=id")
    conn.commit()

def show_data():
    cur.execute("SELECT * FROM account")
    result = cur.fetchall()
    for acc in result:
        print(acc)

def get_data(id):
    data = f"SELECT * FROM account WHERE id = {id}"
    cur.execute(data)
    result = cur.fetchall()
    return result


# show_data()
# deposit(-4300,53)
# show_data()

print(get_data(2))