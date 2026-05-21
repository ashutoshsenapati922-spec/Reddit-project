from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)

class Community(Base):
    __tablename__ = "communities"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    description = Column(Text)

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(Text)
    votes = Column(Integer, default=0)

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    text = Column(Text)
    post_id = Column(Integer, ForeignKey("posts.id"))