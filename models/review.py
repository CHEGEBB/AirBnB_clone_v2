#!/usr/bin/python

"""This is the review module and it contains the Review class
the Review class inherits from the BaseModel class
The Review class represents the review of the place
and it contains the review text and the user id
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import models
import os


class Review(BaseModel, Base):
    """This is the Review class it represents the review of the place
    The Review class inherits from the BaseModel class"""

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'reviews'
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        text = ""
        place_id = ""
        user_id = ""

    def __init__(self, *args, **kwargs):
        """This is the initialization of the Review class
        We use the __init__ method to initialize the Review class
        The __init__ method is a special method in Python
        that is called when an instance (object) of the class is created"""
        super().__init__(*args, **kwargs)
