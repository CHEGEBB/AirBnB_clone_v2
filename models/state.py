#!/usr/bin/python3

"""This is the state module and it contains the State class the State class inherits from the BaseModel class
The State class represents the state of the place and it contains the state name"""

import uuid
from datetime import datetime
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
import os


class State(BaseModel, Base):
    """This is the State class it represents the state of the place
    The State class inherits from the BaseModel class"""

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name = ""

        @property
        def cities(self):
            """This is the getter method for the cities attribute"""
            cities = models.storage.all("City")
            city_list = []
            for city in cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
        
    def __init__(self, *args, **kwargs):
        """This is the initialization of the State class
        We use the __init__ method to initialize the State class
        The __init__ method is a special method in Python that is called when an instance (object) of the class is created"""
        super().__init__(*args, **kwargs)
