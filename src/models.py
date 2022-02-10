#Draw diagram of model: python src/models.py
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'Follower'
    user_from_id = Column(Integer, ForeignKey('User.ID')),
    # user_to_id = Column(Integer, ForeignKey('User.ID')),

    def __repr__(self):
        return '<Follower %r>' % self.user_from_id

    def serialize(self):
        return {
            "user_from_id": self.user_from_id,
            "user_to_id": self.user_to_id
        }

class User(Base):
    __tablename__ = 'User'
    ID = Column(Integer, primary_key=True),
    username = Column(String(80), unique=True, nullable=False),
    firstname = Column(String(80), nullable=False),
    lastname = Column(String(80), nullable=False),
    email = Column(String(80), unique=True, nullable=False),
    child_1 = relationship('Follower', backref="user"),

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "ID": self.ID,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email
        }

class Comment(Base):
    __tablename__ = 'Comment'
    ID = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, nullable=False)
    post_id = Column(Integer, nullable=False)

    def __repr__(self):
        return '<Comment %r>' % self.ID

    def serialize(self):
        return {
            "ID": self.ID,
            "comment_text": self.comment_text,
            "author_id": self.firstname,
            "post_id": self.lastname
        }

class Post(Base):
    __tablename__ = 'Post'
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)

    def __repr__(self):
        return '<Post %r>' % self.ID

    def serialize(self):
        return {
            "ID": self.ID,
            "user_id": self.user_id
        }

class Media(Base):
    __tablename__ = 'Media'
    ID = Column(Integer, primary_key=True)
    type = Column(Enum('video', 'photo'), nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, nullable=False)

    def __repr__(self):
        return '<Media %r>' % self.ID

    def serialize(self):
        return {
            "ID": self.ID,
            "type": self.type,
            "url": self.url,
            "post_id": self.post_id
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')