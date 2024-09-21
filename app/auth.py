from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from .utils import load_users, save_users
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users = load_users()

        print(f"Loaded users: {users}")  # Debug print
        print(f"Attempting login for user: {username}")  # Debug print

        if username in users and check_password_hash(users[username], password):
            session['user'] = username
            flash('Logged in successfully.', 'success')

            return redirect(url_for('tasks.list_tasks'))

        flash('Invalid username or password.', 'error')

    return render_template('login.html')

@auth.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out successfully.', 'success')

    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users = load_users()

        print(f"Current users: {users}")  # Debug print

        if username in users:
            flash('Username already exists.', 'error')
        else:
            users[username] = generate_password_hash(password)

            save_users(users)
            print(f"Updated users: {users}")  # Debug print

            flash('Registered successfully. Please log in.', 'success')
            return redirect(url_for('auth.login'))

    return render_template('register.html')