from flask import Flask, render_template
import psycopg2
from psycopg2 import sql
import os
app = Flask(__name__)

# PostgreSQL database configuration
# PostgreSQL database configuration using environment variables
db_config = {
    'dbname': os.environ.get('DB_NAME', 'postgres'),
    'user': os.environ.get('DB_USER', 'postgres'),
    'password': os.environ.get('DB_PASSWORD', 'mysecretpassword'),
    'host': os.environ.get('DB_HOST', 'localhost'),
    'port': os.environ.get('DB_PORT', '5432'),
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
    app.run(host='0.0.0.0', port=5000, debug=True)
