import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # open the connection to the database
    # conn = sqlite3.connect('my_database.db')
    # conn.row_factory = sqlite3.Row
    # cur = conn.cursor()
    # cur.execute("select * from deployments")
    # rows = cur.fetchall()
    # conn.close()
    return render_template('baseindex.html')

@app.route('/csv1')
def csv1():
    # open the connection to the database
    conn = sqlite3.connect('my_database.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from deployments")
    rows = cur.fetchall()
    conn.close()
    return render_template('index.html', rows=rows)

@app.route('/csv2')
def csv2():
    # open the connection to the database
    conn = sqlite3.connect('my_database.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from deployments")
    rows = cur.fetchall()
    conn.close()
    return render_template('index2.html', rows=rows)