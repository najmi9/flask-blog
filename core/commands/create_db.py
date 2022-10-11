import click
from flask import Blueprint
from sqlalchemy_utils import database_exists, create_database

from core import db

create_db = Blueprint('create_db', __name__)

@create_db.cli.command('create')
def db_create():
    '''Create Database'''

    engine = db.engine

    if not database_exists(engine.url):
        create_database(engine.url)
        db.create_all()
        click.echo(f'database created successfully', color=True)
    else:
        click.echo('Database already exists')


