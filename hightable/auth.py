from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['Get','Post'])
def login():
    return render_template("login.html", boolean="True")

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up', methods = [ 'GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
      
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
      
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if password1 == password2:
          flash("Passwords match")
          # Add registration logic here
        else:
          flash("Passwords do not match!")
    return render_template("sign_up.html")