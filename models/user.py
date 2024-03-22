#!/usr/bin/python3
""" This is the user module. It contains the User class.
This class inherits from BaseModel.
It defines the attributes of the User class.
It also contains the User class methods.
"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
from sqlalchemy.ext.declarative import declarative_base
from models.review import Review

class User(BaseModel, Base):
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from models.place import Place


    def __init__(self, *args, **kwargs):
        """This is the __init__ method.
        It initializes the User class.
        It also checks the environment variable for the type of storage.
        """
        super().__init__(*args, **kwargs)
