#!/usr/bin/python3
"""This module contains the database storage class
This module contains the database storage class.
The DBStorage class manages the database storage.
"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

class DBStorage:
    """This class interacts with the MySQL database
    This class interacts with the MySQL database.
    The DBStorage class manages the
    database storage for the application.
    """
    __engine = None
    __session = None

    def __init__(self):
        """This method instantiates a DBStorage object
        This method instantiates a DBStorage object.
        It creates a new DBStorage object.
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session all objects
        depending on the class name (argument cls)
        """
        new_dict = {}
        if cls:
            if cls == "State":
                from models.state import State
                objs = self.__session.query(State).all()
            else:
                objs = self.__session.query(classes[cls]).all()
            for obj in objs:
                key = "{}.{}".format(cls, obj.id)
                new_dict[key] = obj
        else:
            for c in classes.values():
                if c is not None:
                    objs = self.__session.query(c).all()
                    for obj in objs:
                        key = "{}.{}".format(type(obj).__name__, obj.id)
                        new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """Add the object to the current database session."""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload data from the database."""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """Close the session."""
        self.__session.close()
    
    def close(self):
        """Close the private session attribute."""
        self.__session.remove()
