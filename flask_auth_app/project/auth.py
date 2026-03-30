from flask import Blueprint,render_template,redirect,url_for,request,flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    # login code goes here
     # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Invalid credentials')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.upload'))  # Redirect to upload page after login

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@auth.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    # code to validate and add user to database goes here
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    errors = {}

    if not first_name:
        errors['first_name'] = 'First name required'
    if not last_name:
        errors['last_name'] = 'Last name required'
    if not email or '@' not in email:
        errors['email'] = 'Wrong Email'
    if not password or len(password) < 6:
        errors['password'] = 'Password must be at least 6 characters'
    if password != confirm_password:
        errors['confirm_password'] = 'Wrong Password'

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    user = User.query.filter_by(email=email).first()
    if user:
        errors['email'] = 'Email address already exists'

    if errors:
        for field, msg in errors.items():
            flash(f"{field}:{msg}")
        return redirect(url_for('auth.signup'))

    new_user = User(
        email=email,
        first_name=first_name,
        last_name=last_name,
        password=generate_password_hash(password, method='pbkdf2:sha256')
    )
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))