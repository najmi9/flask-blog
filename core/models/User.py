
from sqlalchemy.sql import func
from flask_login import UserMixin
from core import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), nullable=False)
    roles = db.relationship('Role')
    createdAt = db.Column(db.DateTime(), default=func.now(), nullable=False)
    blog_posts = db.relationship('BlogPost')

    def is_admin(self):
        roleAdmin = filter(lambda userRole : 'ROLE_ADMIN' == userRole.name, self.roles)

        if [] == list(roleAdmin):
            return False

        return True
