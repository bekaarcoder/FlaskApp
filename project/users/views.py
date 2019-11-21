from flask import Blueprint, render_template, redirect, url_for, flash, abort, request
from project import db
from flask_login import login_user, login_required, logout_user
from project.models import User
from project.users.forms import LoginForm, RegistrationForm

users_blueprint = Blueprint('users', __name__, template_folder='templates/users')

@users_blueprint.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You are logged out!")
    return redirect(url_for('index'))

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash("Logged in Successfully!")

            next = request.args.get('next')
            if next == None or not next[0] == '/' or next == '/users/logout':
                next = url_for('users.dashboard')

            return redirect(next)

    return render_template('login.html', form=form)

@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data
        user = User(email, username, password)

        db.session.add(user)
        db.session.commit()
        flash("Registration Successful!")
        return redirect(url_for('users.login'))

    return render_template('register.html', form=form)
