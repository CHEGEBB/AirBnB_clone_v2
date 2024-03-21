#!/usr/bin/python3

"""
This module contains tests for the City class it  tests the City class
for expected behavior and documentation
It tests for the existence of docstrings and adherance to PEP8
"""

from sqlalchemy.ext.declarative import declarative_base
import os
import inspect
import models
import pep8 as pycodestyle
import unittest
from models.base_model import BaseModel
from datetime import datetime
City = models.city.City
module_doc = models.city.__doc__

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    Base = declarative_base()
else:
    Base = object



class TestCityDocs(unittest.TestCase):
    """
    This class tests for City documentation and style
    It tests for the existence of classes, methods and
    functions docstrings and adherence to PEP8
    """

    @classmethod
    def setUpClass(cls):
        """
        This method set the instances to be tested
        It runs before any test
        The instances are the methods in the class
        """
        cls.city_funcs = inspect.getmembers(City, inspect.isfunction)

    def test_pep8_conformance(self):
        """
        This method checks for pep8 conformance
        It will check for PEP8 conformance in the module and the test
        The test uses the pycodestyle library
        """
        for path in ['models/city.py', 'tests/test_models/test_city.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """
        This method checks for the existence of module docstring
        It checks for the presence of a docstring in the module
        """
        self.assertIsNot(module_doc, None,
                         "city.py needs a docstring")
        self.assertTrue(len(module_doc) > 1,
                        "city.py needs a docstring")

    def test_class_docstring(self):
        """
        This method checks for the existence of docstrings in City class
        It checks for the presence of a docstring in the City class
        """
        self.assertIsNot(City.__doc__, None,
                         "City class needs a docstring")
        self.assertTrue(len(City.__doc__) >= 1,
                        "City class needs a docstring")

    def test_func_docstrings(self):
        """
        This method checks for the presence of docstrings in City methods
        It checks for the presence of docstrings
        in all the methods of the class
        The docstrings should be present and of a certain length
        """
        for func in self.city_funcs:
            with self.subTest(function=func):
                self.assertIsNot(
                    func[1].__doc__,
                    None,
                    "{:s} method needs a docstring".format(func[0])
                )
                self.assertTrue(
                    len(func[1].__doc__) > 1,
                    "{:s} method needs a docstring".format(func[0])
                )


class TestCity(unittest.TestCase):
    """
    This class tests the City class
    It tests for the existence of the City instance
    It tests for the proper instantiation of the City instance
    It tests for the inheritance of the City class
    It tests for the attributes of the City class
    """

    def test_instantiation(self):
        """
        This method checks for the existence of the City instance
        It checks if the City instance is properly instantiated
        """
        my_city = City()
        self.assertIsInstance(my_city, City)
        my_city.name = "San Francisco"
        self.assertEqual(my_city.name, "San Francisco")
        self.assertIsInstance(my_city.created_at, datetime)
        self.assertIsInstance(my_city.updated_at, datetime)
        self.assertIsInstance(my_city.id, str)
        self.assertEqual(str(my_city.__class__),
                         "<class 'models.city.City'>")
        self.assertEqual(my_city.__class__.__name__, "City")
        self.assertTrue(issubclass(my_city.__class__, City))
        self.assertTrue(issubclass(my_city.__class__,
                                   models.base_model.BaseModel))

    def test_is_subclass(self):
        """
        This method checks for the inheritance of the City class
        It checks if City class is a subclass of BaseModel
        """
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_name_attr(self):
        """
        This method checks for the name attribute of the City class
        It checks if the city has the name attribute
        The name attribute is an empty string
        """
        city = City()
        self.assertTrue(hasattr(city, "name"))
        if models.storage_t == 'db':
            self.assertEqual(city.name, None)
        else:
            self.assertEqual(city.name, "")

    def test_state_id_attr(self):
        """
        This method checks for the state_id attribute of the City class
        It checks if the city has the state_id attribute
        The state_id attribute is an empty string
        """
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        if models.storage_t == 'db':
            self.assertEqual(city.state_id, None)
        else:
            self.assertEqual(city.state_id, "")

    def test_to_dict_creates_dict(self):
        """
        This method checks for the to_dict method of the City class
        It checks if the output is as expected
        The to_dict method should return a dictionary with key value pairs
        """
        c = City()
        new_d = c.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in c.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """
        This method checks for the to_dict method of the City class
        It checks if the output is as expected
        The to_dict method should return a dictionary with key value pairs
        """
        c = City()
        new_d = c.to_dict()
        self.assertEqual(new_d["__class__"], "City")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        for attr in c.__dict__:
            if attr is not "_sa_instance_state":
                self.assertEqual(new_d[attr], c.__dict__[attr])

    def test_str(self):
        """
        This method checks for the __str__ method of the City class
        It checks if the output is in the specified format
        The method is used to print an object
        """
        c = City()
        string = "[City] ({}) {}".format(c.id, c.__dict__)
        self.assertEqual(string, str(c))


if __name__ == "__main__":
    unittest.main()
