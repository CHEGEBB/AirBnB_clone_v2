#!/usr/bin/python3
"""This module contains the FileStorage class
This module contains the FileStorage class.
The FileStorage class manages the file storage.
"""
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import json
from os import path
from models.base_model import BaseModel
from models.user import User

classes = {"BaseModel": BaseModel, "User": User, "State": State,
           "City": City, "Place": Place, "Amenity": Amenity,
           "Review": Review}


class FileStorage:
    """This class interacts with the JSON file system
    This class interacts with the JSON file system.
    The FileStorage class manages the JSON file storage for the application.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """This method queries the current database session
        This method queries the current database session.
        It retrieves objects from the database session.
        """
        if cls is None:
            return self.__objects
        new_dict = {}
        for key, value in self.__objects.items():
            if isinstance(value, cls):
                new_dict[key] = value
        return new_dict

    def new(self, obj):
        """This method adds a new object to the current database session
        This method adds a new object to the current database session.
        It adds a new object to the database session.
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """This method saves the current database session to the file system
        This method saves the current database session to the file system.
        It saves the current database session to the file system.
        """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(new_dict, f)

    def reload(self):
        """This method loads the current database session from the file system
        This method loads the current database session from the file system.
        It loads the current database session from the file system.
        """
        if path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                new_dict = json.load(f)
            for key, value in new_dict.items():
                cls = value['__class__']
                obj = classes[cls](**value)
                self.__objects[key] = obj

    def delete(self, obj=None):
        """This method deletes an object from the current database session
        This method deletes an object from the current database session.
        It deletes an object from the database session.
        """
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """This method calls the reload method
        This method calls the reload method.
        It reloads the database session from the file system.
        """
        self.reload()
