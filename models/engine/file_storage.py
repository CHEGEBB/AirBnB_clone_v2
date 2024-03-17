#!/usr/bin/python3
""""Module to manage file storage for hbnb clone """
import json


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file
    to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w") as f:
            obj_dict = {key: obj.to_dict() for key,
                        obj in self.__objects.items()}
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            from models.base_model import BaseModel
            from models.user import User
            from models.amenity import Amenity
            from models.city import City
            from models.place import Place
            from models.review import Review
            from models.state import State
            classes = {"BaseModel": BaseModel, "User": User,
                       "Amenity": Amenity, "City": City,
                       "Place": Place, "Review": Review, "State": State}

            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    obj = classes[value["__class__"]](**value)
                    self.all()[key] = obj
        except FileNotFoundError:
            pass
