#!/usr/bin/python3

""""This is the amenity module and it contains the
Amenity class that inherits from BaseModel
It also contains the Amenity class that inherits from Base
and links to the amenities table in the database
"""


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
import sqlalchemy
import os
import models


class Amenity(BaseModel, Base):

    """Representation of Amenity
    Attributes:
        __tablename__ (str): The name of the table
        name (sqlalchemy string): The name of the amenity
        place_amenities (sqlalchemy relationship): The relationship between the
        place and the amenity
    """

    __tablename__ = "amenities"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """This is the initialization of the Amenity class"""
        super().__init__(*args, **kwargs)
