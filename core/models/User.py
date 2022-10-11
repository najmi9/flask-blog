
from pickle import FALSE
from sqlalchemy.sql import func
from flask_login import UserMixin
from sqlalchemy.dialects.mysql import LONGTEXT

from core import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), nullable=False)
    roles = db.Column(LONGTEXT(charset='utf8mb4', collation='utf8mb4_unicode_ci'))
    createdAt = db.Column(db.DateTime(), default=func.now(), nullable=False)
    blog_posts = db.relationship('BlogPost')

    def is_admin(self):
        if None == self.roles:
            return False

        if 'ROLE_ADMIN' in self.roles:
            return True

        return FALSE
