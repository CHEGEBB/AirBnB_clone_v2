#!/usr/bin/python3
""""Review class inheriting from BaseModel class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
