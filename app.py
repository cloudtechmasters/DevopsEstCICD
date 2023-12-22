from flask import Flask, render_template
import psycopg2
from psycopg2 import sql

app = Flask(__name__)

# PostgreSQL database configuration
db_config = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'mysecretpassword',
    'host': '3.84.157.208',
    'port': '5432',
}

# Route to fetch data from PostgreSQL and render HTML template
@app.route('/')
def index():
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    # Fetch data from the clients table
    query = sql.SQL("SELECT * FROM {}").format(sql.Identifier('clients'))
    cursor.execute(query)
    clients_data = cursor.fetchall()

    conn.close()

    return render_template('index.html', clients_data=clients_data)

if __name__ == '__main__':
    app.run(debug=True)
