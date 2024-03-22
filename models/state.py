#!/usr/bin/python3
"""This module contains the State class that inherits from BaseModel
It is the State of the HBnB project
It is a class that defines the State
"""

from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models.base_model import Base

class State(BaseModel, Base):
    """This is the State class
    It is the State of the HBnB project
    It is a class that defines the State
    """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
        @property
        def cities(self):
            """This is a getter attribute that returns the list of City instances
            It is a getter attribute that returns the list of City instances
            """
            city_list = []
            from models import storage
            for city in storage.all('City').values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list

        
    def __init__(self, *args, **kwargs):
        """This initializes the State instance
        It is the initialization of the State instance
        The State instance is initialized
        """
        super().__init__(*args, **kwargs)
