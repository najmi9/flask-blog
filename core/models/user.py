'''User table'''

from sqlalchemy import Column, Integer, String, DateTime, func
from flask_login import UserMixin
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from core import db

class User(db.Model, UserMixin):
    '''
        roles column is table of roles like: ROLE_USER, ROLE_ADMIN
        the admin has a role ROLE_ADMIN
        else are all normal users
    '''
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    password = Column(String(255), nullable=False)
    roles = Column(LONGTEXT(charset='utf8mb4', collation='utf8mb4_unicode_ci'))
    createdAt = Column(DateTime(), default=func.now(), nullable=False)
    blog_posts = relationship('BlogPost')

    def is_admin(self):
        '''Check if a user has the role ROLE_ADMIN'''
        if None is self.roles:
            return False

        if 'ROLE_ADMIN' in self.roles:
            return True

        return False
