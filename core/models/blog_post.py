'''blog post'''

from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, func
from core import db

class BlogPost(db.Model):
    '''This is represent an article in the db'''

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    createdAt = Column(DateTime(True), default=func.now(),nullable=False)
    updatedAt = Column(DateTime(True), default=func.now(),nullable=False)
    image = Column(String(255))
    user_id = Column(Integer, ForeignKey('user.id'))
