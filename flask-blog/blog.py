#!/usr/bin/env python
from flask import Flask, render_template, request, session, flash, redirect
from flask import url_for, g
import sqlite3

# configuration
DATABASE = "blog.db"
USERNAME = "admin"
PASSWORD = "admin"
SECRET_KEY = "hard_to_guess"


app = Flask(__name__)

# pull in app configuration by looking UPPERCASE variable
app.config.from_object(__name__)


def connect_db():
    """ function used for connecting to the database """
    return sqlite3.connect(app.config['DATABASE'])


@app.route("/", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
            error = "Invalid Credentials. Please try again."
        else:
            sesion['logged_in'] = True
            return redirect(url_for('main'))
    return render_template('login.html', error=error)


@app.route("/main")
def main():
    return render_template('main.html')


if __name__ == "__main__":
    app.run(debug=True)