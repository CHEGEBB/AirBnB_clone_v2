#!/usr/bin/python3

"""This is the place module and it contains the Place class
The Place class inherits from the BaseModel class
"""

import os
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    Base = declarative_base()
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))
else:
    Base = BaseModel


class Place(Base):
    """This is the Place class it represents the place
    The Place class inherits from the BaseModel class"""

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
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
        amenities = relationship("Amenity",secondary=place_amenity,
                                  viewonly=False)
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
            reviews = models.storage.all("Review")
            review_list = []
            for review in reviews.values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """This is the getter method for the amenities attribute"""
            amenities = models.storage.all("Amenity")
            amenity_list = []
            for amenity in amenities.values():
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, obj):
            """This is the setter method for the amenities attribute"""
            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)
            else:
                pass

    def __init__(self, *args, **kwargs):
        """This is the initialization of the Place class
        We use the __init__ method to initialize the Place class
        The __init__ method is a special method in Python that is
        called when an instance (object) of the class is created"""
        super().__init__(*args, **kwargs)
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.amenity_ids = []
