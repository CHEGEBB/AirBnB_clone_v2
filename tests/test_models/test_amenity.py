#!/usr/bin/python3

"""
This module contains the test for the Amenity class
It is a unit test module that defines test cases for the Amenity class
It makes use of the unittest module to test the
functionality of the Amenity class.
"""

import os
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import models
from models import amenity
from models.base_model import BaseModel
import inspect
import pep8
from datetime import datetime
Amenity = amenity.Amenity

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    Base = declarative_base()
else:
    Base = object

class TestAmenity(unittest.TestCase):
    """
    This class defines the test suite for the Amenity class
    It makes use of the unittest module to test the
    functionality of the Amenity class.
    """
    @classmethod
    def setUpClass(cls):
        """This method is called to prepare the test fixture.
        It creates an instance of the Amenity
        class that can be used in the test methods.
        """
        cls.amenity = Amenity()
        cls.amenity.name = "Breakfast"

    @classmethod
    def teardown(cls):
        """This method is called after the test methods have been called.
        It is used to clean up the test fixture.
        """
        del cls.amenity

    def test_amenity_pep8_conformance(self):
        """The test_amenity_pep8_conformance tests the
        amenity.py file for PEP8 conformance.
        It uses the pep8 module to validate
        the conformity of amenity.py with PEP8.
        """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_amenity_pep8_conformance_test(self):
        """The test_amenity_pep8_conformance_test tests
        the test_amenity.py file for PEP8 conformance.
        It uses the pep8 module to validate the
        conformity of test_amenity.py with PEP8.
        """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_amenity_module_docstring(self):
        """The test_amenity_module_docstring tests
        the amenity.py file for a docstring.
        It checks if the amenity.py file has a docstring.
        """
        self.assertIsNot(amenity.__doc__, None,
                         "amenity.py needs a docstring")
        self.assertTrue(len(amenity.__doc__) >= 1,
                        "amenity.py needs a docstring")

    def test_amenity_class_docstring(self):
        """The test_amenity_class_docstring
        tests the Amenity class for a docstring.
        It checks if the Amenity class has a docstring.
        """
        self.assertIsNot(Amenity.__doc__, None,
                         "Amenity class needs a docstring")
        self.assertTrue(len(Amenity.__doc__) >= 1,
                        "Amenity class needs a docstring")

    def test_amenity_func_docstrings(self):
        """The test_amenity_func_docstrings
        tests the presence of docstrings in Amenity methods.
        It checks if all the methods of the Amenity class have docstrings.
        """
        for func in self.amenity.__dir__():
            self.assertIsNot(func.__doc__, None,
                             "{:s} method needs a docstring".format(func))
            self.assertTrue(len(func.__doc__) >= 1,
                            "{:s} method needs a docstring".format(func))

    def test_is_subclass(self):
        """The test_is_subclass tests that Amenity is a subclass of BaseModel.
        It checks if the Amenity class is a subclass of the BaseModel class.
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_name_attr(self):
        """
        The test_name_attr tests that the name attribute
        of Amenity is a string.
        It checks if the name attribute of the Amenity class is a string.
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

    def test_to_dict_creates_dict(self):
        """The test_to_dict_creates_dict tests
        that the to_dict method creates a dictionary with proper attributes.
        It checks if the to_dict method creates a dictionary
        with proper attributes.
        """
        am = Amenity()
        new_d = am.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in am.__dict__:
            if attr != 'updated_at' and attr != 'created_at':
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """The test_to_dict_values tests that the
        values in the dictionary returned from to_dict are correct.
        It checks if the values in the dictionary returned
        from to_dict are correct.
        The test checks if the values in the dictionary
        are of the correct type.
        """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        am = Amenity()
        new_d = am.to_dict()
        self.assertEqual(new_d["__class__"], "Amenity")
        self.assertEqual(new_d["created_at"], am.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], am.updated_at.strftime(t_format))
        self.assertEqual(new_d["id"], am.id)

    def test_str(self):
        """The test_str tests the __str__ method of the Amenity class.
        It checks if the __str__ method of the Amenity class returns a string.
        """
        amenity = Amenity()
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))

    def test_name(self):
        """The test_name tests that the name attribute of Amenity is a string.
        It checks if the name attribute of the Amenity class is a string.
        """
        amenity = Amenity()
        self.assertEqual(type(amenity.name), str)
