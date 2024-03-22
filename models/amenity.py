#!/usr/bin/python
""" holds class Amenity"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class Amenity(BaseModel, Base):
    """Representation of Amenity """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity")
    else:
        name = ""

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def place_amenities(self):
            """getter attribute returns the list of City instances with state_id"""
            list_amenities = []
            for key, value in models.storage.all().items():
                if value.__class__.__name__ == 'Place' and value.amenity_id == self.id :
                    list_amenities.append(value)
            return list_amenities
        
        @place_amenities.setter
        def place_amenities(self, obj):
            """setter attribute links the place_amenity relationship"""
            if obj.__class__.__name__ == 'Place':
                self.place_amenities.append(obj)

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
