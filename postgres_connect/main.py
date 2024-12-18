import psycopg2
import config

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
    print(row)