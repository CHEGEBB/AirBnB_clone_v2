#!/usr/bin/python3

"""This is the user module.
It includes the class User.
This class is associated with the class Place and the class Review.

"""

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from models.base_model import Base
from models.base_model import BaseModel


class User(BaseModel, Base):
    """This is the class for User
    It is associated with the class Place and the class Review.
    This class defines users table in MySQL database.
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")