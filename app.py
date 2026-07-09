from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)

def check_db_status():
    try:
        conn = psycopg2.connect(
            host=os.environ.get('DB_HOST'),
            dbname=os.environ.get('DB_NAME'),
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASSWORD'),
            port=os.environ.get('DB_PORT', 5432),
            connect_timeout=3
        )
        conn.close()
        return "Connected"
    except Exception as e:
        return f"Not connected ({e})"

@app.route('/')
def home():
    db_status = check_db_status()
    return render_template('index.html', message='Hello, World!', db_status=db_status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)