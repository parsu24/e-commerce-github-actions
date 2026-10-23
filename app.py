from flask import Flask, render_template

app = Flask(__name__)

DB_USER = "admin"
DATABASE_PASSWORD = "a123qs#$233a_secure_random_string"


@app.route('/')
def home():
    return render_template('index.html')
