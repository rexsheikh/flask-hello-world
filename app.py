import psycopg2
from flask import Flask
app = Flask(__name__)

DB_URL = "postgresql://lab10_db_a716_user:g6SPYI7LZQtAbN2frAolICbLQa9uzY4K@dpg-d49p823ipnbc73974hrg-a/lab10_db_a716"

def get_conn():
    return psycopg2.connect(DB_URL)

@app.route('/')
def hello_world():
    return 'Hello world from Rex in CSPB 3308'

@app.route('/db_test')
def db_test():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT 1;')
    cur.close()
    conn.close()
    return "Database connection successful"

@app.route('/db_create')
def db_create():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
        );
    ''')
    conn.commit()
    cur.close()
    conn.close()
    return "Basketball table created"

@app.route('/db_insert')
def db_insert():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        VALUES
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    cur.close()
    conn.close()
    return "Basketball Table Populated"

@app.route('/db_select')
def db_select():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Basketball;')
    records = cur.fetchall()
    cur.close()
    conn.close()

    html_parts = [
        '<table border="1" cellpadding="6">',
        '<thead><tr><th>First</th><th>Last</th><th>City</th><th>Name</th><th>Number</th></tr></thead>',
        '<tbody>'
    ]
    for row in records:
        html_parts.append('<tr>')
        for cell in row:
            html_parts.append(f'<td>{cell}</td>')
        html_parts.append('</tr>')
    html_parts.append('</tbody></table>')
    return ''.join(html_parts)

@app.route('/db_drop')
def db_drop():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('DROP TABLE Basketball;')
    conn.commit()
    cur.close()
    conn.close()
    return "Basketball Table Dropped"
