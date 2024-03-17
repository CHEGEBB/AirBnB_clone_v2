#!/usr/bin/python3
""""City class inheriting from BaseModel class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class that inherits from BaseModel"""
    state_id = ""
    name = ""
