#!/usr/bin/python3

"""This module entails the City class that inherits from BaseModel and Base and represents the city of a state"""

from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.place import place_amenity

# This class inherits from BaseModel and Base and represents the city of a state
class City(BaseModel, Base):

    """This class represents the city of a state and inherits from BaseModel and Base"""
    if models.storage_t == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):

        """This method initializes the City class and its attributes"""
        super().__init__(*args, **kwargs)
