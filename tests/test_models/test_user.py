#!/usr/bin/python3

"""
This module contains the test for the User class
The test ensures the User class is working as expected.
It includes test cases for the attributes and methods of the User class.
"""
from sqlalchemy.ext.declarative import declarative_base
import os
from datetime import datetime
import inspect
import models
from models import user
from models.base_model import BaseModel
import pep8
import unittest

User = user.User

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    Base = declarative_base()
else:
    Base = object


class TestUserDocs(unittest.TestCase):
    """
    This class contains test cases for the User class in the models module.
    It includes test cases for the User class documentation and style.
    """

    @classmethod
    def setUpClass(cls):
        """
        This method is used to prepare the test fixture.
        It ensures the User class is ready for testing.
        """
        cls.user_f = inspect.getmembers(User, inspect.isfunction)

    def test_pep8_conformance_user(self):
        """
        This method checks for PEP8 conformance in the User class.
        It ensures the User class conforms to PEP8 standards.
        """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_user(self):
        """
        This method checks for PEP8 conformance in the test_user.py file.
        It ensures the test_user.py file conforms to PEP8 standards.
        """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_user_module_docstring(self):
        """
        This method tests for the presence
        of a docstring in the user.py module.
        It ensures the user.py module has a docstring.
        """
        self.assertIsNot(user.__doc__, None,
                         "user.py needs a docstring")
        self.assertTrue(len(user.__doc__) >= 1,
                        "user.py needs a docstring")

    def test_user_class_docstring(self):
        """
        This method tests for the presence of a docstring in the User class.
        It ensures the User class has a docstring.
        """
        self.assertIsNot(User.__doc__, None,
                         "User class needs a docstring")
        self.assertTrue(len(User.__doc__) >= 1,
                        "User class needs a docstring")

    def test_user_func_docstrings(self):
        """
        This method tests for the presence of docstrings in User methods.
        It ensures all methods in the User class have docstrings.
        """
        for func in self.user_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestUser(unittest.TestCase):
    """
    This class contains test cases for the User class.
    It includes test cases for the attributes and methods of the User class.
    The test cases ensure the User class is working as expected.
    """

    def test_is_subclass(self):
        """
        This method tests that User is a subclass of BaseModel.
        It ensures the User class is a subclass of BaseModel.
        """
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

    def test_email(self):
        """
        This method tests the email attribute.
        It ensures the User class has an email attribute.
        """
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")

    def test_password(self):
        """
        This method tests the password attribute.
        It ensures the User class has a password attribute.
        """
        user = User()
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")

    def test_first_name(self):
        """
        This method tests the first_name attribute.
        It ensures the User class has a first_name attribute.
        """
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")

    def test_last_name(self):
        """
        This method tests the last_name attribute.
        It ensures the User class has a last_name attribute.
        """
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")

    def test_str(self):
        """
        This method tests the str method.
        It ensures the str method produces the correct output.
        """
        user = User()
        string = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(string, str(user))

    def test_to_dict(self):
        """
        This method tests the to_dict method.
        It ensures the to_dict method produces the correct output.
        """
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(user_dict["id"], user.id)
        self.assertEqual(user_dict["created_at"], user.created_at.isoformat())
        self.assertEqual(user_dict["updated_at"], user.updated_at.isoformat())
        self.assertEqual(user_dict["email"], user.email)
        self.assertEqual(user_dict["password"], user.password)
        self.assertEqual(user_dict["first_name"], user.first_name)
        self.assertEqual(user_dict["last_name"], user.last_name)
