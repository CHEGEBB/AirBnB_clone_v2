#!/usr/bin/python3

"""
This module contains tests for the Place class it  tests the Place class
for expected behavior and documentation
It tests for the existence of docstrings and adherance to PEP8
"""

import inspect
import models
from models import place
import pep8 as pycodestyle
import unittest
from models.base_model import BaseModel
from datetime import datetime
from unittest import mock
Place = models.place.Place
module_doc = models.place.__doc__


class TestPlaceDocs(unittest.TestCase):
    """This class tests for Place documentation and style
    It tests for the existence of classes, methods and
    functions docstrings and adherance to PEP8
    """

    @classmethod
    def setUpClass(self):
        """This method set the instances to be tested
        It runs before any test
        The instances are the methods in the class
        """
        self.place_funcs = inspect.getmembers(Place, inspect.isfunction)

    def test_pep8_conformance(self):
        """This method checks for pep8 conformance
        It will check for PEP8 conformance in the module and the test
        The test uses the pycodestyle library
        """
        for path in ['models/place.py',
                     'tests/test_models/test_place.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """This method checks for the existence of module docstring
        It checks for the presence of a docstring in the module
        """
        self.assertIsNot(module_doc, None, "place.py needs a docstring")
        self.assertTrue(len(module_doc) > 1, "place.py needs a docstring")

    def test_class_docstring(self):
        """This method checks for the existence of docstrings in Place class
        It checks for the presence of a docstring in the Place class
        """
        self.assertIsNot(Place.__doc__, None, "Place class needs a docstring")
        self.assertTrue(len(Place.__doc__) >= 1,
                        "Place class needs a docstring")

    def test_func_docstrings(self):
        """This method checks for the existence of docstrings in Place methods
        It checks for the presence of a docstring in the methods of the class
        """
        for func in self.place_funcs:
            with self.subTest(func=func):
                self.assertIsNot(func[1].__doc__, None,
                                 "{} method needs a docstring".format(func[0]))
                self.assertTrue(len(func[1].__doc__) >= 1,
                                "{} method needs a docstring".format(func[0]))


class TestPlace(unittest.TestCase):

    def test_is_subclass(self):
        """
        This method checks if Place is a subclass of BaseModel
        Place should be a subclass of BaseModel
        """
        self.assertTrue(issubclass(Place, BaseModel))

    def test_fields(self):
        """This method checks the fields in Place class
        The Place class should have the following fields
        city_id, user_id, name, description, number_rooms, number_bathrooms
        max_guest, price_by_night, latitude, longitude, amenity_ids
        """
        place = Place()
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, list)

    def test_place_type(self):
        """This method checks the type of place
        The place should be of type Place
        """
        place = Place()
        self.assertEqual(type(place), Place)

    def test_place_id(self):
        """This method checks the type of id
        The id should be a string
        """
        place = Place()
        self.assertEqual(type(place.id), str)

    def test_created_at(self):
        """This method checks the type of created_at
        The created_at should be a datetime object
        """
        place = Place()
        self.assertEqual(type(place.created_at), datetime)

    def test_updated_at(self):
        """This method checks the type of updated_at
        The updated_at should be a datetime object
        """
        place = Place()
        self.assertEqual(type(place.updated_at), datetime)

    def test_str_method(self):
        """This method checks the str method
        The str method should return a string
        """
        place = Place()
        string = str(place)
        self.assertEqual(type(string), str)

    def test_to_dict_method(self):
        """This method checks the to_dict method
        The to_dict method should return a dictionary
        """
        place = Place()
        place_dict = place.to_dict()
        self.assertEqual(type(place_dict), dict)
        place_class = place_dict['__class__']
        self.assertEqual(place_class, 'Place')

    def test_to_dict_attr(self):
        """This method checks the to_dict method
        The to_dict method should return a
        dictionary with the following attributes
        id, created_at, updated_at, __class__
        """
        place = Place()
        place_dict = place.to_dict()
        self.assertTrue('id' in place_dict)
        self.assertTrue('created_at' in place_dict)
        self.assertTrue('updated_at' in place_dict)
        self.assertTrue('__class__' in place_dict)

    def test_str(self):
        """This method checks for the __str__ method of the Place class
        It checks if the output is in the specified format
        The method is used to print an object
        """
        place = Place()
        string = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(string, str(place))

    def test_save(self):
        """
        This method checks for the save method of the Place class
        It checks if the attribute updated_at is updated
        """
        place = Place()
        old_updated_at = place.updated_at
        place.save()
        self.assertNotEqual(old_updated_at, place.updated_at)

    def test_kwargs(self):
        """
        This method checks for the kwargs argument of the Place class
        It checks if the class can be instantiated with the kwargs
        """
        place = Place()
        place.name = "House"
        place.save()
        place_dict = place.to_dict()
        place_json = Place(**place_dict)
        self.assertEqual(place_json.name, "House")
        self.assertEqual(place_json.__class__.__name__, "Place")
        self.assertIsInstance(place_json, Place)
        self.assertEqual(place_json.to_dict()['name'], "House")
        self.assertEqual(place_json.to_dict()['id'], place.id)
        self.assertEqual(place_json.to_dict()['created_at'],
                         place.created_at.isoformat())
        self.assertEqual(place_json.to_dict()['updated_at'],
                         place.updated_at.isoformat())
        self.assertEqual(place_json.to_dict()['__class__'],
                         "Place")
        self.assertEqual(place_json.to_dict()['city_id'], place.city_id)
        self.assertEqual(place_json.to_dict()['user_id'], place.user_id)
        self.assertEqual(place_json.to_dict()['description'],
                         place.description)
        self.assertEqual(place_json.to_dict()['number_rooms'],
                         place.number_rooms)
        self.assertEqual(place_json.to_dict()['number_bathrooms'],
                         place.number_bathrooms)
        self.assertEqual(place_json.to_dict()['max_guest'],
                         place.max_guest)
        self.assertEqual(place_json.to_dict()['price_by_night'],
                         place.price_by_night)
        self.assertEqual(place_json.to_dict()['latitude'],
                         place.latitude)
        self.assertEqual(place_json.to_dict()['longitude'],
                         place.longitude)
        self.assertEqual(place_json.to_dict()['amenity_ids'],
                         place.amenity_ids)

    def test_city_id_attr(self):
        """
        This method checks for the city_id attribute of the Place class
        It checks if the place has the city_id attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        if models.storage_t == 'db':
            self.assertEqual(place.city_id, None)
        else:
            self.assertEqual(place.city_id, "")

    def test_user_id_attr(self):
        """This method checks for the user_id attribute of the Place class
        It checks if the place has the user_id attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))
        if models.storage_t == 'db':
            self.assertEqual(place.user_id, None)
        else:
            self.assertEqual(place.user_id, "")

    def test_name_attr(self):
        """
        This method checks for the name attribute of the Place class
        It checks if the place has the name attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        if models.storage_t == 'db':
            self.assertEqual(place.name, None)
        else:
            self.assertEqual(place.name, "")

    def test_description_attr(self):
        """
        This method checks for the description attribute of the Place class
        It checks if the place has the description attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "description"))
        if models.storage_t == 'db':
            self.assertEqual(place.description, None)
        else:
            self.assertEqual(place.description, "")

    def test_number_rooms_attr(self):
        """
        This method checks for the number_rooms attribute of the Place class
        It checks if the place has the number_rooms attribute
        """

        place = Place()
        self.assertTrue(hasattr(place, "number_rooms"))
        if models.storage_t == 'db':
            self.assertEqual(place.number_rooms, None)
        else:
            self.assertEqual(type(place.number_rooms), int)
            self.assertEqual(place.number_rooms, 0)

    def test_number_bathrooms_attr(self):
        """Test Place has attr number_bathrooms, and it's an int == 0"""
        place = Place()
        self.assertTrue(hasattr(place, "number_bathrooms"))
        if models.storage_t == 'db':
            self.assertEqual(place.number_bathrooms, None)
        else:
            self.assertEqual(type(place.number_bathrooms), int)
            self.assertEqual(place.number_bathrooms, 0)

    def test_max_guest_attr(self):
        """This method checks for the max_guest attribute of the Place class
        It checks if the place has the max_guest attribute
        """
        self.assertTrue(hasattr(place, "max_guest"))
        if models.storage_t == 'db':
            self.assertEqual(place.max_guest, None)
        else:
            self.assertEqual(type(place.max_guest), int)
            self.assertEqual(place.max_guest, 0)

    def test_price_by_night_attr(self):
        """This method checks for the price_by_night
        attribute of the Place class
        It checks if the place has the price_by_night attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "price_by_night"))
        if models.storage_t == 'db':
            self.assertEqual(place.price_by_night, None)
        else:
            self.assertEqual(type(place.price_by_night), int)
            self.assertEqual(place.price_by_night, 0)

    def test_latitude_attr(self):
        """Test Place has attr latitude, and it's a float == 0.0"""
        place = Place()
        self.assertTrue(hasattr(place, "latitude"))
        if models.storage_t == 'db':
            self.assertEqual(place.latitude, None)
        else:
            self.assertEqual(type(place.latitude), float)
            self.assertEqual(place.latitude, 0.0)

    def test_longitude_attr(self):
        """Test Place has attr longitude, and it's a float == 0.0"""
        place = Place()
        self.assertTrue(hasattr(place, "longitude"))
        if models.storage_t == 'db':
            self.assertEqual(place.longitude, None)
        else:
            self.assertEqual(type(place.longitude), float)
            self.assertEqual(place.longitude, 0.0)

    @unittest.skipIf(models.storage_t == 'db', "not testing File Storage")
    def test_amenity_ids_attr(self):
        """Test Place has attr amenity_ids, and it's an empty list"""
        place = Place()
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertEqual(type(place.amenity_ids), list)
        self.assertEqual(len(place.amenity_ids), 0)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        p = Place()
        new_d = p.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in p.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        p = Place()
        new_d = p.to_dict()
        self.assertEqual(new_d["__class__"], "Place")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], p.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], p.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        place = Place()
        string = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(string, str(place))
