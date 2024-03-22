#!/usr/bin/python

""" This is the amenity module and it contains the Amenity class
The Amenity class inherits from the BaseModel class
"""

from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
import models
from sqlalchemy.orm import relationship
import os
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """This is the Amenity class it represents the amenity
    The Amenity class inherits from the BaseModel class
    It defines the attributes of the Amenity class
    """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """This method initializes the Amenity instance
        It calls the __init__ method of the super class
        """
        super().__init__(*args, **kwargs)
