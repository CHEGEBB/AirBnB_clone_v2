#!/usr/bin/python3

"""This is the user module.It contains the User class.
This class inherits from BaseModel.
It defines the attributes of the User class.
It also contains the User class methods.
"""

from models.base_model import BaseModel
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class User(BaseModel, Base):
    """This is the User class.
    It inherits from BaseModel.
    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

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
        """This is the __init__ method.
        It is the initializer of the User class.
        It calls the super class initializer.
        It also checks the environment variable for the type of storage.
        """
        super().__init__(*args, **kwargs)
