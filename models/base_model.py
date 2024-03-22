#!/usr/bin/python3
"""This is the base model class for AirBnB"""
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid

Base = declarative_base()
time_format = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """This class defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Instantiation of base model class"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.created_at = datetime.utcnow() if not kwargs.get("created_at") else \
                               datetime.strptime(kwargs["created_at"], time_format)
            self.updated_at = datetime.utcnow() if not kwargs.get("updated_at") else \
                               datetime.strptime(kwargs["updated_at"], time_format)
            self.id = str(uuid.uuid4()) if not kwargs.get("id") else kwargs["id"]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.utcnow()

    def __str__(self):
        """Return string representation"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Save the object to storage"""
        self.updated_at = datetime.utcnow()
        from models import storage
        storage.new(self)
        storage.save()

    def __repr__(self):
        """Return a string representation"""
        return self.__str__()

    def to_dict(self):
        """Return a dictionary representation"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.strftime(time_format)
        new_dict["updated_at"] = self.updated_at.strftime(time_format)
        new_dict["__class__"] = self.__class__.__name__
        return new_dict

    def delete(self):
        """Delete the object from storage"""
        from models import storage
        storage.delete(self)
