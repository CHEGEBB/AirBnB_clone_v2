#!/usr/bin/python3

"""This is the file storage module and it contains the FileStorage class
The FileStorage class serializes instances to a JSON file and deserializes
JSON file to instances
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This is the FileStorage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This is the all method
        It returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """This is the new method
        It sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """This is the save method
        It serializes __objects to the JSON file (path: __file_path)
        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(new_dict, f)

    def reload(self):
        """This is the reload method
        It deserializes the JSON file to __objects (only if the JSON file exists)
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as f:
                new_dict = json.load(f)
            for key, value in new_dict.items():
                cls_name = key.split(".")[0]
                cls = eval(cls_name)
                obj = cls(**value)
                FileStorage.__objects[key] = obj 

    def delete(self, obj=None):
        """This is the delete method
        It deletes obj from __objects if it’s inside
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]
                self.save()

    def close(self):
        """This is the close method
        It calls reload method for deserializing the JSON file to objects
        """
        self.reload()
