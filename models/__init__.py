#!/usr/bin/python3
from models.user import User
from model.state import State
from models.city import city
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv

if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()

"""
This file indicates the presence of a python package
It creates the variable storage used to save instances
"""
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
