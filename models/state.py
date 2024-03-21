#!/usr/bin/python3
"""This is the state module and it contains the State class
The State class inherits from the BaseModel class
It contains the class definition for the State class
"""

from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
import models
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """Representation of state """
    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if os.getenv('HBNB_TYPE_STORAGE') != "db":
        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
