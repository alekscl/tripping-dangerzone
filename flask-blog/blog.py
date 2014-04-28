#!/usr/bin/env python
from flask import Flask, render_template, request, session, flash, redirect
from flask import url_for, g
import sqlite3

# configuration
DATABASE = "blog.db"


app = Flask(__name__)

# pull in app configuration by looking UPPERCASE variable
app.config.from_object(__name__)


def connect_db():
    """ function used for connecting to the database """
    return sqlite3.connect(app.config['DATABASE'])


@app.route("/")
def login():
    return render_template('login.html')


@app.route("/main")
def main():
    return render_template('main.html')


if __name__ == "__main__":
    app.run(debug=True)
