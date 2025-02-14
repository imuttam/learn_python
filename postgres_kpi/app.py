from flask import Flask, render_template
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

# Database connection parameters
db_user = "postgres"
db_password = "xxxxx"  # Replace with your actual password
db_host = "localhost"  # or your database host
db_port = "5432"       # default PostgreSQL port
db_name = "kpi"

# Database connection configuration
db_config = {
    "dbname": "kpi",
    "user": "postgres",
    "password": "Cell0ne",
    "host": "localhost",
    "port": "5432"
}

def get_db_connection():
    conn = psycopg2.connect(**db_config)
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM tcs_kpi;')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
