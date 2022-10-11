
from flask import Blueprint, flash, redirect, render_template, url_for
from flask import request
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from core.forms.login_form import LoginForm
from core.forms.registration_form import RegistrationForm
from core.models.user import User
from core import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if 'POST' == request.method and form.validate():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()

        if None is user or False is check_password_hash(user.password, password):
            flash('Bad Credentials', 'danger')
        else:
            login_user(user)
            flash('User logged in successfully', 'success')
            return redirect(url_for('views.home'))

    return render_template(
        'auth/login.html',
        form=form
    )

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if 'POST' == request.method and form.validate():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        user = User(
            email=form.email.data,
            password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash('User created successfully', 'success')

        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form)


@auth.route('logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
