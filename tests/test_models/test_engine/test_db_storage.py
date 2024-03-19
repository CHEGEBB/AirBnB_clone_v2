#!/usr/bin/python3

"""This module is the test for the db_storage module
This is the test for the db_storage module. It tests the db_storage module
to ensure that it works as expected
 """

import unittest
import os
import pep8
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from os import getenv
import models
import inspect
from models.engine import db_storage
from models.amenity import Amenity


DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class TestDBStorageDocs(unittest.TestCase):
    """This class defines the test for the db_storage module
    This class contains tests to ensure that the db_storage module is working as expected
    It tests the documentation and style of the db_storage module
    """
    @classmethod
    def setUpClass(cls):
        """This method sets up the tests
        It sets up the tests by creating an instance of the DBStorage class
        """
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """This method tests the pep8 style of the db_storage module
        It tests the db_storage module to ensure that it conforms to the PEP8 style
        The test uses the pep8 module
        """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """This method tests the pep8 style of the test_db_storage module
        It tests the test_db_storage module to ensure that it conforms to the PEP8 style
        The test uses the pep8 module
        """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """This method tests the docstring of the db_storage module
        It tests the db_storage module to ensure that it has a docstring
        """
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """This method tests the docstring of the DBStorage class
        It tests the DBStorage class to ensure that it has a docstring
        The test uses the inspect module
        and the DBStorage class
        """
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """This is a test for the docstrings in DBStorage methods
        This test checks for the presence of docstrings in DBStorage methods
        Returns:
            True if all methods have docstrings or False if not
        """
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

class TestFileStorage(unittest.TestCase):
    """This is the TestFileStorage class
    This class contains tests for the FileStorage class
    The tests will make sure that the FileStorage class is working as expected
    """
    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """The all method should return a dictionary
        This test checks to make sure that the all method returns a dictionary"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """This is a test for the all method
        This test checks to make sure that the all method returns all instances of a given class
        """

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_new(self):
        """This is a test for the new method
        This test checks to make sure that the new method adds a new instance to the session
        """

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_save(self):
        """This is a test for the save method
        This test checks to make sure that the save method saves the session to the database
        It saves the session to the database in the form of a dictionary
        """
