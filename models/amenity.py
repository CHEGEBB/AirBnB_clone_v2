#!/usr/bin/python3

"""This module entails the Amenity class that inherits from BaseModel"""
# Importing the necessary modules
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from models.place import place_amenity
from sqlalchemy.orm import relationship

# We check if the storage type is equal to db, if it is we create the table amenities
class Amenity(BaseModel, Base):
    """This class is for the amenities of the places it is related to the Place class"""

    if models.storage_t == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Here we initialize the Amenity class that inherits from BaseModel"""
        super().__init__(*args, **kwargs)
