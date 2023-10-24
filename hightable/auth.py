from flask import Blueprint, render_template, request, flash, session

import mysql.connector

auth = Blueprint('auth', __name__)

security = mysql.connector.connect(
    host='aws.connect.psdb.cloud',
    user='h9cuwub11kz3kl7naeag',
    password='pscale_pw_lPBxSR4iIWGiy9hcJxk9tgAN1XptSU0dU5BqoETceNy',
    database='hightable')


@auth.route('/login', methods=['Get', 'Post'])
def login():
  if request.method == 'POST':
    scursor = security.cursor()

    username = request.form.get('username')
    password = request.form.get('password')

    scursor.execute("SELECT * FROM security WHERE username=%s AND password=%s",
                    (username, password,))

    record = scursor.fetchone()

    if record:
      if (record[1] == username):
        if (record[2] == password):
          flash('You have been logged in!')
          session['loggedin'] = True
          session['username'] = record[1]
          return render_template("login.html", boolean="True")
        else:
          flash('Invalid password')
      else:
        flash('Invalid username')
  return render_template("login.html")


@auth.route('/logout')
def logout():
  return "<p>logout</p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
  if request.method == 'POST':
    firstName = request.form.get('firstName')
    lastName = request.form.get('lastName')

    dataOfBirth = request.form.get('dataOfBirth')
    email = request.form.get('email')
    phone = request.form.get('phone')
    mailing = request.form.get('mailing')

    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    if password1 == password2:
      flash("Passwords match")
      # Add registration logic here
    else:
      flash("Passwords do not match!")
  return render_template("sign_up.html")
