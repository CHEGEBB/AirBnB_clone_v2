#!/usr/bin/python3

"""This module entails the Amenity class that inherits from BaseModel"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """This class is for the amenities of the places"""

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def place_amenities(self):
            """Getter for place_amenities"""
            place_amenities = []
            for place in list(models.storage.all("Place").values()):
                if self.id in place.amenity_ids:
                    place_amenities.append(place)
            return place_amenities
    else:
        place_amenities = relationship("Place", secondary=place_amenity)

    def __init__(self, *args, **kwargs):
        """Initializes Amenity"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """String representation of Amenity"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def place_amenities(self):
            """Getter for place_amenities"""
            place_amenities = []
            for place in list(models.storage.all("Place").values()):
                if self.id in place.amenity_ids:
                    place_amenities.append(place)
            return place_amenities
    else:
        place_amenities = relationship("Place", secondary=place_amenity)

    def __init__(self, *args, **kwargs):
        """Initializes Amenity"""
        super().__init__(*args, **kwargs)
        