#!/usr/bin/python3

"""This is the init file of the models module it contains the storage instance
The storage instance is a FileStorage instance
It is a dictionary that holds all the instances of the classes
"""

from os import getenv
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import models
from models.city import City
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

if getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()

Base = declarative_base()

class State(BaseModel, Base):
    """This is the state class
    The state class inherits from the BaseModel class
    """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            city_list = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
