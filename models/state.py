#!/usr/bin/python3

"""This module contains the State class that inherits from BaseModel
It is the State of the HBnB project
It is a class that defines the State
"""
#importing modules while avoiding circular imports
from models.base_model import BaseModel
import models
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os

class State(BaseModel):
    """This is the State class
    It is the State of the HBnB project
    It is a class that defines the State
    """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """This is a getter attribute that returns the list of City instances
            It is a getter attribute that returns the list of City instances
            """
            city_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
        

    def __init__(self, *args, **kwargs):
        """This initializes the State instance
        It is the initialization of the State instance
        The State instance is initialized
        """
        super().__init__(*args, **kwargs)
