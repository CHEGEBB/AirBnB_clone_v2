#!/usr/bin/python3

"""This module contains the State class that inherits from BaseModel
It is the State of the HBnB project
It is a class that defines the State
"""

# Importing modules while avoiding circular imports
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
from models.city import City 
from models import storage
from models import models

# Import the Base from sqlalchemy.ext.declarative
from sqlalchemy.ext.declarative import declarative_base

# Define the declarative base
Base = declarative_base()

class State(BaseModel, Base):
    """This is the State class
    It is the State of the HBnB project
    It is a class that defines the State
    """
    __tablename__ = 'states'  # Define the table name

    # Define the name column
    name = Column(String(128), nullable=False)

    # Define the relationship with City
    cities = relationship("City", backref="state")

    # Define the cities property only if using file storage
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

    # Define the __init__ method
    def __init__(self, *args, **kwargs):
        """This initializes the State instance
        It is the initialization of the State instance
        The State instance is initialized
        """
        super().__init__(*args, **kwargs)
