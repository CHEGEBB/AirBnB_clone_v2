#!/usr/bin/python3

"""This module contains test cases for the
State class in the models module.
The test cases ensures the State class is working as expected.
It also ensures the attributes and
methods of the State class are working as expected.
"""
from sqlalchemy.ext.declarative import declarative_base
import os
import unittest
from models.state import State
from models.base_model import BaseModel
import inspect
import pep8
from models import state
import models
State = State

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    Base = declarative_base()
else:
    Base = object


class TestState(unittest.TestCase):
    """This class contains test cases for the State class
    It includes test cases for the
    attributes and methods of the State class.
    The test cases ensures the State class is working as expected.
    """
    @classmethod
    def setUpClass(cls):
        """This method is used to prepare the test fixture.
        It ensures the State class is ready for testing.
        The method is called before any test
        case of the TestState class is run.
        """
        cls.state_f = inspect.getmembers(State, inspect.isfunction)

    def test_pep8_conformance_state(self):
        """This method checks for PEP8 conformance in the State class.
        It ensures the State class conforms to PEP8 standards.
        """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_state(self):
        """This method checks for PEP8 conformance in the test_state.py file.
        It ensures the test_state.py file conforms to PEP8 standards.
        """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_state_module_docstring(self):
        """This method tests for the presence
        of a docstring in the state.py module.
        It ensures the state.py module has a docstring.
        """
        self.assertIsNot(state.__doc__, None,
                         "state.py needs a docstring")
        self.assertTrue(len(state.__doc__) >= 1,
                        "state.py needs a docstring")

    def test_state_class_docstring(self):
        """This method tests for the presence
        of a docstring in the State class.
        It ensures the State class has a docstring.
        """
        self.assertIsNot(State.__doc__, None,
                         "State class needs a docstring")
        self.assertTrue(len(State.__doc__) >= 1,
                        "State class needs a docstring")

    def test_state_class_docstring(self):
        """This method tests for the
        presence of a docstring in the State class.
        It ensures the State class has a docstring.
        """
        self.assertIsNot(State.__doc__, None,
                         "State class needs a docstring")
        self.assertTrue(len(State.__doc__) >= 1,
                        "State class needs a docstring")

    def test_state_func_docstrings(self):
        """This method tests for the presence of docstrings in State methods.
        It ensures the methods of the State class have docstrings.
        """
        for func in self.state_f:
            self.assertIsNot(func.__doc__, None,
                             "{} method needs a docstring".format(func))
            self.assertTrue(len(func.__doc__) >= 1,
                            "{} method needs a docstring".format(func))


class TestState(unittest.TestCase):
    """This class contains test cases for the State class
    It includes test cases for the attributes and methods of the State class.
    The test cases ensures the State class is working as expected.
    """
    def test_is_subclass(self):
        """This method tests if State is a subclass of BaseModel
        It ensures the State class is a subclass of BaseModel.
        The test passes if State is a subclass of BaseModel.
        """
        state = State()
        self.assertTrue(issubclass(state.__class__, BaseModel), True)

    def test_name_attr(self):
        """This method tests if State has an
        attribute name, and it's an empty string
        It ensures the State class has an
        attribute name, and it's an empty string by default.
        The test passes if the attribute
        is present and it's an empty string.
        """
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def test_to_dict_creates_dict(self):
        """This method tests if to_dict
        method creates a dictionary with proper attrs
        It ensures the to_dict method creates
        a dictionary with the proper attributes.
        The test passes if the dictionary is
        created and the attributes are correct.
        """
        s = State()
        d = s.to_dict()
        self.assertEqual(type(d), dict)
        for attr in s.__dict__:
            self.assertTrue(attr in d)
        self.assertTrue("__class__" in d)
        self.assertTrue(d["__class__"] == "State")
        self.assertTrue(d["created_at"] == s.created_at.isoformat())
        self.assertTrue(d["updated_at"] == s.updated_at.isoformat())

    def test_to_dict_values(self):
        """This method tests if values in dict
        returned from to_dict are correct
        It ensures the values in the dictionary
        returned from the to_dict method are correct.
        The test passes if the values are correct.
        """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        s = State()
        new_d = s.to_dict()
        self.assertEqual(new_d["__class__"], "State")
        self.assertEqual(new_d["created_at"], s.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], s.updated_at.strftime(t_format))
        self.assertEqual(new_d["created_at"], s.created_at.isoformat())
        self.assertEqual(new_d["updated_at"], s.updated_at.isoformat())

    def test_str(self):
        """This method tests the __str__ method of the State class
        It ensures the __str__ method of the
        State class is working as expected.
        The test passes if the __str__ method
        returns the expected string.
        """
        s = State()
        string = "[State] ({}) {}".format(s.id, s.__dict__)
        self.assertEqual(string, str(s))
