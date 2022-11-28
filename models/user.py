#!/usr/bin/python3
"""this is a user class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """this is a class for the user
    Attributes:
        __tablename__: table of users
        email: email address of the user
        password: password for login
        first_name: first name
        last_name: last name
    """
    __tablename__ = "users"
    email = Column("emial", String(128), nulable=False)
    password = Column("password", String(128), nullable=False)
    first_name = Column("first_name", String(128), nullable=True)
    last_name = Column("last_name", String(128), nullable=True)
    places = relationship('Place', backref='user')
    reviews = relationship('Review', backref='user')
