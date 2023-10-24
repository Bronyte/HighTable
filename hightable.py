import sqlite3

from flask import Flask, g, redirect, render_template, request, session, url_for, flash
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user


app = Flask(__name__)


@app.route('/home')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods = ['POST'])
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/forgot-password')
def forgot_psswd():
    return render_template('forgot_psswd.html')

if __name__ == '__main__':
    app.run(debug=True)
