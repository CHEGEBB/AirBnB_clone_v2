#!/usr/bin/python3

"""This module contains the test for the console module
This module contains the test for the console module.
The test ensures the console module is working as expected.
"""

import unittest
import os
import pep8
import inspect
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class TestConsoleDocs(unittest.TestCase):
    """This class contains test cases for the console module
    This class contains test cases for the console module in the console module.
    It includes test cases for the console module documentation and style.
    """

    @classmethod
    def setUpClass(cls):
        """This method is used to prepare the test fixture
        This method is used to prepare the test fixture.
        It ensures the console module is ready for testing.
        """
        cls.console_f = inspect.getmembers(HBNBCommand, inspect.isfunction)

    def test_pep8_conformance_console(self):
        """This method checks for PEP8 conformance in the console module.
        It ensures the console module conforms to PEP8 standards.
        """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """This method checks for PEP8 conformance in the test_console.py file.
        It ensures the test_console.py file conforms to PEP8 standards.
        """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """This method tests for the presence of a docstring in the console module.
        It ensures the console module has a docstring.
        """
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "console.py needs a docstring")
        
    def test_console_class_docstring(self):
        """This method tests for the presence of a docstring in the HBNBCommand class.
        It ensures the HBNBCommand class has a docstring.
        """
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")
        
    def test_console_methods_docstrings(self):
        """This method tests for the presence of docstrings in HBNBCommand methods.
        It ensures all methods in the HBNBCommand class have docstrings.
        """
        for func in self.console_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]) )
            
class TestConsole(unittest.TestCase):
    """This class contains test cases for the console module
    This class contains test cases for the console module in the console module.
    It includes test cases for the console module attributes and methods.
    The test cases ensures the console module is working as expected.
    """

    @classmethod
    def setUpClass(cls):
        """This method is used to prepare the test fixture
        This method is used to prepare the test fixture.
        It ensures the console module is ready for testing.
        """
        cls.console = HBNBCommand()

    def test_create(self):
        """This method tests the create method of the console.
        It ensures the create method of the console works as expected.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.assertTrue(len(f.getvalue()) > 0)

    def test_show(self):
        """This method tests the show method of the console.
        It ensures the show method of the console works as expected.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_destroy(self):
        """This method tests the destroy method of the console.
        It ensures the destroy method of the console works as expected.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_all(self):
        """This method tests the all method of the console.
        It ensures the all method of the console works as expected.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
            self.assertEqual(f.getvalue(), "[]\n")

    def test_update(self):
        """This method tests the update method of the console.
        It ensures the update method of the console works as expected.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_quit(self):
        """This method tests the quit method of the console.
        It ensures the quit method of the console works as expected.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("quit")
            self.assertTrue(len(f.getvalue()) > 0)

    def test_EOF(self):
        """This method tests the EOF method of the console.
        It ensures the EOF method of the console works as expected.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))

    def test_emptyline(self):
        """This method tests the emptyline method of the console.
        It ensures the emptyline method of the console works as expected.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("\n"))

    def test_create_instance(self):
        """This method tests the create method of the console.
        It ensures the create method of the console works as expected.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.assertTrue(len(f.getvalue()) > 0)

    def test_show_instance(self):
        """This method tests the show method of the console.
        It ensures the show method of the console works as expected.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_destroy_instance(self):
        """This method tests the destroy method of the console.
        It ensures the destroy method of the console works as expected.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_all_instance(self):
        """This method tests the all method of the console.
        It ensures the all method of the console works as expected.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
            self.assertEqual(f.getvalue(), "[]\n")

    def test_update_instance(self):
        """This method tests the update method of the console.
        It ensures the update method of the console works as expected.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
