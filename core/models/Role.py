from sqlalchemy import ForeignKey
from core import db

class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
    user_id = db.Column(db.Integer(), ForeignKey('user.id'))
