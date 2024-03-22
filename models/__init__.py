#!/usr/bin/python3

"""This is the init file of the models module it contains the storage instance
and the methods to interact with the storage instance
It also contains the classes that inherit from the BaseModel class
"""

from os import getenv
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

if getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()

def close(self):
    """This method calls the close method on the storage instance
    It calls the close method on the storage instance
    """
    storage.close()

def reload(self):
    """This method calls the reload method on the storage instance
    It calls the reload method on the storage instance"""
    storage.reload()

def all(self):
    """This method calls the all method on the storage instance
    It calls the all method on the storage instance"""
    return storage.all()

def new(self, obj):
    """This method calls the new method on the storage instance
    It calls the new method on the storage instance
    """
    storage.new(obj)

def save(self):
    """This method calls the save method on the storage instance
    It calls the save method on the storage instance
    you can call this method to save the changes to the JSON file   
    """
    storage.save()

def delete(self, obj=None):
    """This method calls the delete method on the storage instance
    It calls the delete method on the storage instance
    This method deletes an object from the dictionary
    """
    storage.delete(obj)

def get(self, cls, id):
    """This method calls the get method on the storage instance
    """
    return storage.get(cls, id)
