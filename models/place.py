#!/usr/bin/python3

"""
This is the place module that holds the Place class, which is holds the data of the places in the app.
"""
# Import the necessary modules
from models.base_model import BaseModel
from models.city import City
from models.user import User
import models
import os
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv

# Create a variable for the storage type
if models.storage_type == 'db':
    place_amenity = Table('place_amenity', models.storage.Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
                      )


# Create the Place class
class Place(BaseModel, models.storage.Base):
    """This is the class for the Place object."""
    if models.storage_type == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenities = relationship('Amenity', secondary=place_amenity, viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
# this is the getter for the reviews
        def __init__(self, *args, **kwargs):
            """This is the initialization of the Place object."""
            super().__init__(*args, **kwargs)

            if models.storage_type != 'db':
                @property
                def reviews(self):
                    """This gets the list of Review instances where place_id is equal to the current Place.id."""
                    review_list = []
                    for review in models.storage.all('Review').values():
                        if review.place_id == self.id:
                            review_list.append(review)
                    return review_list
                
                @property
                def amenities(self):
                    """This gets the list of Amenity instances where amenity_id is equal to the current Place.id."""
                    amenity_list = []
                    for amenity in models.storage.all('Amenity').values():
                        if amenity.id in self.amenity_ids:
                            amenity_list.append(amenity)
                    return amenity_list
