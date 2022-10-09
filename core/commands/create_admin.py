import click
from flask import Blueprint
from matplotlib import use
from werkzeug.security import generate_password_hash

from core.models.User import User
from core.models.Role import Role
from core import db

ROLE_NAME='ROLE_ADMIN'

create_admin = Blueprint('create_admin', __name__)

@create_admin.cli.command('create')
def newAdmin():
    '''Create new admin'''
    email = click.prompt('The email of the admin ')
    password = click.prompt('The password of the admin ', hide_input=True)

    user = User(
        email=email,
        password=generate_password_hash(password)
    )

    user.roles.append(Role(name=ROLE_NAME))

    db.session.add(user)
    db.session.commit()

    click.echo(f'Admin with email: "{email}" created successfully', color=True)
