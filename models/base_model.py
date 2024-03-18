#!/usr/bin/python3

"""This module entails the BaseModel class"""

# Importing the necessary modules
from datetime import datetime
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid
# The time variable is equal to the format of the time
time = "%Y-%m-%dT%H:%M:%S.%f"
# We check if the storage type is equal to db, if it is we create the table amenities
if models.storage_t == "db":
    Base = declarative_base()
else:
    Base = object

# The BaseModel class from which future classes will be derived HERE we check if the storage type is equal to db, if it is we create the table amenities
class BaseModel:

    """This class is the base model for all other classes it contains the id, created_at, and updated_at attributes and methods for the other classes to inherit from it"""
    if models.storage_t == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)


# The BaseModel class from which future classes will be derived
    def __init__(self, *args, **kwargs):

        """Here we initialize the BaseModel class that will be inherited by other classes"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """returns a string representation of the instance object in the format: [<class name>] (<self.id>) <self.__dict__>"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)
# 
    def save(self):
        """This method updates the public instance attribute updated_at with the current datetime when the object is changed and saves the object to the storage"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)