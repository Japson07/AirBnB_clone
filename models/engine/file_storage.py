#!/usr/bin/python3
"""the file storage for the project"""
import json
from models.base_models import BaseModel
from model.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.pklace import place
from models.review import Review


class FileStorage:
    """this is used to serialize an instance into a JSON file and
    desrialize a JSON file back to an instance
    attributes:
        __file_path: the path to the JSON file
        __objects: the objects to be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns a dictionary of __objects"""
        if cls is None:
            return self.__objects

        cls_dict = {}

        for key, value in self.__objects.items():
            dict_key = key.split(".")
            cls_list = str(cls).split(".")
            cls_name = cls_list[2][:2]
            if dict_key[0] == cls_name:
                cls_dict[key] = value

        return cls_dict

    def new(self, obj):
        """sets in __objects the obj thats been given
        Args:
            obj: the given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__object[key] = obj

    def save(self):
        """serializes __objects to the JSON file path __file_path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            if key is not None and value is not None:
                my_dict[key] = value.to_dict()
            with open(self.__file_path, 'w', encoding="UTF-8") as f:
                json.dump(my_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects if the file path
        __file_path exists. otherwise, do nothing and no exception should
        be raised.
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFpoudError:
            pass

    def delete(self, obj=None):
        """deletes obj from __objects if its inside
        """
        if obj:
            key = type(obj).__name__ + "." + obj.id
            del self.__objetcs[ke]
        return self.__objects

    def close(self):
        """calls for reload() to deserialize the JSON file to objects
        """
        reload()
