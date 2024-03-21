#!/usr/bin/python3
"""This module contains the database storage class
This module contains the database storage class.
The DBStorage class manages the database storage.
"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.amenity import Amenity
from models.base_model import Base
from models.state import State
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review

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
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """This method queries the current database session
        This method queries the current database session.
        It retrieves objects from the database session.
        """
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """This method adds the object to the current database session
        This method adds the object to the current database session.
        It adds a new object to the database session.
        """
        self.__session.add(obj)

    def save(self):
        """This method commits all changes of the current database session
        This method commits all changes of the current database session.
        It saves all changes to the database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """This method deletes from the current database session obj if not None
        This method deletes from the current database session obj if not None.
        It deletes an object from the database session.
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """This method reloads data from the database
        This method reloads data from the database.
        It creates all tables in the database.
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """This method calls remove() method on the private session attribute
        This method calls remove() method on the private session attribute.
        It removes the session from the database.
        """
        self.__session.remove()
