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
    
def close():
    """This method calls the close method on the storage instance"""
    storage.close()

def reload():
    """This method calls the reload method on the storage instance"""
    storage.reload()

def all():
    """This method calls the all method on the storage instance"""
    return storage.all()

def new(obj):
    """This method calls the new method on the storage instance"""
    storage.new(obj)

def save():
    """This method calls the save method on the storage instance"""
    storage.save()

def delete(obj=None):
    """This method calls the delete method on the storage instance"""
    storage.delete(obj)

def get(cls, id):
    """This method calls the get method on the storage instance"""
    return storage.get(cls, id)
