from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['Get','Post'])
def login():
    
    return render_template("login.html", boolean="True")

@auth.route('/logout')
def logout():
    return "<p>logout </p>"

@auth.route('/sign-up')
def sign_up():
    if request.method == 'POST':
        email = request.form.get(email)
        firstName = request.form.get('password1')

    return render_template("sign_up.html")