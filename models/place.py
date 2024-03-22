#!/usr/bin/python3

"""This is the place module and it contains the Place class
The Place class inherits from the BaseModel class
"""

import os
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models


class Place(BaseModel, Base):
    """This is the Place class, it represents the place.
    The Place class inherits from the BaseModel and Base classes"""

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
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

        reviews = relationship("Review", backref="place", cascade="all, delete")
        amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)

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

        @property
        def reviews(self):
            """This is the getter method for the reviews attribute"""
            all_reviews = models.storage.all(models.Review)
            place_reviews = [review for review in all_reviews.values() if review.place_id == self.id]
            return place_reviews

        @property
        def amenities(self):
            """This is the getter method for the amenities attribute"""
            all_amenities = models.storage.all(models.Amenity)
            place_amenities = [amenity for amenity in all_amenities.values() if amenity.place_id == self.id]
            return place_amenities

        @amenities.setter
        def amenities(self, obj):
            """This is the setter method for the amenities attribute"""
            if isinstance(obj, models.Amenity):
                obj.place_id = self.id
                models.storage.new(obj)
                models.storage.save()

class User(BaseModel, Base):
    """This is the User class, it represents a user."""
    __tablename__ = 'users'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        places = relationship("Place", backref="user", cascade="all, delete")
    else:
        @property
        def places(self):
            """This is the getter method for the places attribute"""
            all_places = models.storage.all(Place)
            user_places = [place for place in all_places.values() if place.user_id == self.id]
            return user_places

class City(BaseModel, Base):
    """This is the City class, it represents a city."""
    __tablename__ = 'cities'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        places = relationship("Place", backref="cities", cascade="all, delete")
    else:
        @property
        def places(self):
            """This is the getter method for the places attribute"""
            all_places = models.storage.all(Place)
            city_places = [place for place in all_places.values() if place.city_id == self.id]
            return city_places
