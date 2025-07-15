import MySQLdb
from flask import Flask, redirect, render_template, request, url_for
import mysql.connector
from flask_mysqldb import MySQL


app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)
