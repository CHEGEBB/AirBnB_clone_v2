#!/usr/bin/python3
""""User class inheriting from BaseModel class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
