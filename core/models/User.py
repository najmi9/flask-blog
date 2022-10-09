
from sqlalchemy.sql import func
from flask_login import UserMixin
from core import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), nullable=False)
    roles = db.Column(db.ARRAY(db.String), default=['ROLE_USER'])
    createdAt = db.Column(db.DateTime(), default=func.now())
    blog_posts = db.relationship('BlogPost')
