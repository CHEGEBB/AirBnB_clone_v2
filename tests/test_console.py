#!/usr/bin/python3
"""This module contains the test for the console module
This module contains the test for the console module.
The test ensures the console module is working as expected.
"""

from io import StringIO
from unittest.mock import patch
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
import unittest
import pep8
import inspect
import console
from console import HBNBCommand
import os
import json
import sys
from models.amenity import Amenity
from models.review import Review


class TestConsoleDocs(unittest.TestCase):
    """This class contains test cases for the console module
    This class contains test cases for the console module in the console module.
    It includes test cases for the console module documentation and style.
    """
    def test_pep8_conformance_console(self):
        """This method checks for PEP8 conformance in the console module.
        It ensures the console module conforms to PEP8 standards.
        """
        result = pep8.Checker(['console.py']).check_all()
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """This method checks for PEP8 conformance in the test_console.py file.
        It ensures the test_console.py file conforms to PEP8 standards.
        """
        result = pep8.Checker(['tests/test_console.py']).check_all()
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """This method checks for the console.py module docstring
        It ensures the console.py module has a docstring.
        """
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """This method checks for the HBNBCommand class docstring
        It ensures the HBNBCommand class has a docstring.
        """
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")
