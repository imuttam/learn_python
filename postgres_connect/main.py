import psycopg2
import config
from datetime import datetime

conn = psycopg2.connect(
                    dbname=config.db_name, 
                    user=config.db_user, 
                    password=config.db_password, 
                    host=config.db_host, 
                    port=config.db_port 
                    )
    
query = "SELECT * from actor;"

cur = conn.cursor()
cur.execute(query)
rows = cur.fetchall()
for row in rows:
    print(row[0],row[1],row[2],row[3].strftime('%d-%m-%Y'))

column_names = [desc[0] for desc in cur.description]
print("Column names:", column_names)

cur.close()
conn.close()