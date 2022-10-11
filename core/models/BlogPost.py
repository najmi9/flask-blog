from core import db
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, func


class BlogPost(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    createdAt = Column(DateTime(True), default=func.now(),nullable=False)
    updatedAt = Column(DateTime(True), default=func.now(),nullable=False)
    likes = Column(Integer, nullable=False, default=0)
    image = Column(String(255))
    user_id = Column(Integer, ForeignKey('user.id'))
