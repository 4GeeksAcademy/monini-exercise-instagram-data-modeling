import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Post(Base):
    __tablename__="post"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    media_id = Column(Integer, ForeignKey("media.id"))

class Comment(Base):
    __tablename__="comment"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("post.id"))
    text = Column(String(500), nullable=False)

class Media(Base):
    __tablename__="media"
    id = Column(Integer, primary_key=True)
    URL = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey("post.id"))
    user_id = Column(Integer, ForeignKey("user.id"))

class Followers(Base):
    __tablename__="followers"
    id = Column(Integer, primary_key=True)
    follower_id = Column(Integer, ForeignKey("user.id"))
    following_id = Column(Integer, ForeignKey("user.id"))





    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
