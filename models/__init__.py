#!/usr/bin/python3

"""This is the init file of the models module it contains the storage instance"""

from os import getenv
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

if getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
    
def close(self):
    """This method calls the close method on the storage instance"""
    self.storage.close()

def reload(self):
    """This method calls the reload method on the storage instance"""
    self.storage.reload()

def all(self):
    """This method calls the all method on the storage instance"""
    return self.storage.all()

def new(self, obj):
    """This method calls the new method on the storage instance"""
    self.storage.new(obj)

def save(self):
    """This method calls the save method on the storage instance"""
    self.storage.save()

def delete(self, obj=None):
    """This method calls the delete method on the storage instance"""
    self.storage.delete(obj)

def get(self, cls, id):
    """This method calls the get method on the storage instance"""
    return self.storage.get(cls, id)

