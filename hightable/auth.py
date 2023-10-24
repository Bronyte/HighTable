from flask import Blueprint, render_template, request, flash

import mysql.connector

auth = Blueprint('auth', __name__)

security = mysql.connector.connect(
    host='aws.connect.psdb.cloud',
    user='nvyobhtr1gds29cb71ox',
    password='pscale_pw_kOzcnqONM68bbfjNFvdTyYZQJ02ynHMQaOyVWeF2oF8',
    database='hightable')


@auth.route('/login', methods=['Get', 'Post'])
def login():
  if request.method == 'POST':
    scursor = security.cursor()

    username = request.form.get('userName')
    password = request.form.get('password')

    scursor.execute("SELECT password FROM security WHERE username = %s",
                    (username, ))

    result = scursor.fetchone()

    if result:
      if (result[0] == password):
        flash('You have been logged in!')
        return render_template("login.html", boolean="True")
      else:
        flash('Invalid username or password')
        return render_template("login.html", boolean="False")

  return render_template("login.html", boolean="False")


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
