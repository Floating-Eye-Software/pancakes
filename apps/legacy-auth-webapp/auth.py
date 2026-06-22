from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from data import db

# https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login
# https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    success = db.check_password(username, password)
    if success:
        user = db.get_user(username)
        login_user(user, remember=remember)
        return redirect(url_for('user.dashboard'))
    else:
        flash('Login attempt failed')
        return redirect(url_for('auth.login'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    username = request.form.get('username')
    password = request.form.get('password')
    success = db.sign_up_user(username, password)
    if success:
        flash('Account created. Please login.')
        return redirect(url_for('auth.login'))
    else:
        flash('That username is unavailable')
        return redirect(url_for('auth.signup'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('public.index'))
