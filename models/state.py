#!/usr/bin/python3

"""This module contains the State class that inherits from BaseModel."""

from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import os
import models
from models.city import City

from models.base_model import BaseModel

Base = declarative_base()  # Moved Base definition to the top

class State(BaseModel, Base):
    """Represents a State in the HBnB project."""
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    # Getter for cities, only used for file storage
    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Returns a list of City instances associated with this State."""
            city_list = [city for city in models.storage.all(City).values()
                          if city.state_id == self.id]
            return city_list


    # Define the __init__ method
    def __init__(self, *args, **kwargs):
        """This initializes the State instance
        It is the initialization of the State instance
        The State instance is initialized
        """
        super().__init__(*args, **kwargs)
