#!/usr/bin/python3

"""This is the base model module and it contains the BaseModel
 class the amenity class inherits from this class
 It also contains the Base class that links to the
 amenities table in the database
 """

import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
import models
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """This is the BaseModel class it  acts as the base
    class for all other classes in the project
    It is the foundation of the project
    """

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime,
                            default=datetime.utcnow(), nullable=False)
        updated_at = Column(DateTime,
                            default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """This is the initialization of the BaseModel class
           when an instance (object) of the class is created
          """

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != "__class__":
                    setattr(self, key, value)
            if 'id' not in kwargs:
                setattr(self, 'id', str(uuid.uuid4()))
            time = datetime.now()
            if 'created_at' not in kwargs:
                setattr(self, 'created_at', time)
            if 'updated_at' not in kwargs:
                setattr(self, 'updated_at', time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """This is the string representation of the BaseModel class
        We use the __str__ method to return a
        string representation of the BaseModel class
        The __str__ method is a special method
        in Python that is called by the
         print() function
        """

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """This saves the BaseModel instance
        to the storage using the storage instance
        We use the save method to save
        the BaseModel instance to the storage
          using the storage instance
          """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def __repr__(self) -> str:
        """returns
        """
        return self.__str__()

    def to_dict(self):
        """This returns a dictionary representation of the BaseModel class
            A dictionary of all the key values in __dict__
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """This deletes the current instance from the storage
        This deletes the current instance from the storage
            it uses the delete method from the storage instance
        """
        models.storage.delete(self)
        models.storage.save()
