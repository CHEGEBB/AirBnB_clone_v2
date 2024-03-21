#!/usr/bin/python3

"""This is the city module and it contains the City class the
city class inherits from the base model class
    The City class represents the city of the place"""

from models.base_model import BaseModel, Base
import models
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from os import getenv


class City(BaseModel, Base):

    """This is the City class it represents the city of the place
    The City class inherits from the BaseModel class"""

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities", cascade="all, delete")
    else:
        name = ""
        state_id = ""

        @property
        def places(self):
            """This is the getter method for the places attribute"""
            places = models.storage.all("Place")
            place_list = []
            for place in places.values():
                if place.city_id == self.id:
                    place_list.append(place)
            return place_list

    def __init__(self, *args, **kwargs):
        """This is the initialization of the City class
        We use the __init__ method to initialize the City class
        The __init__ method is a special method in Python that is called
        when an instance (object) of the class is created"""
        super().__init__(*args, **kwargs)
