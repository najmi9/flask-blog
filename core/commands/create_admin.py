import click
from flask import Blueprint
from werkzeug.security import generate_password_hash

from core.models.User import User
from core import db

ROLE_NAME='ROLE_ADMIN'

create_admin = Blueprint('create_admin', __name__)

@create_admin.cli.command('create')
def new_admin():
    '''Create new admin'''
    email = click.prompt('The email of the admin ')
    password = click.prompt('The password of the admin ', hide_input=True)

    user = User(
        email=email,
        password=generate_password_hash(password, method='sha256'),
        roles=f'["{ROLE_NAME}"]'
    )

    db.session.add(user)
    db.session.commit()

    click.echo(f'Admin with email: "{email}" created successfully', color=True)
