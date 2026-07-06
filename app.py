from flask import Flask, render_template
import psycopg2, os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', message="Studenthub is live on AWS!")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)
