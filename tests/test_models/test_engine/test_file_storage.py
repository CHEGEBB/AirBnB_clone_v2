#!/usr/bin/python3

"""This module contains the test for the file_storage module
This module contains the test for the file_storage module.
The test ensures the file_storage module is working as expected.
"""

import unittest
import pep8
import inspect
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
import inspect
import os
import models
import json
FileStorage = models.engine.file_storage.FileStorage
classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class TestFileStorageDocs(unittest.TestCase):
    """This class contains test cases for the file_storage module
    This class contains test cases for the file_storage module in the file_storage module.
    It includes test cases for the file_storage module documentation and style.
    """

    @classmethod
    def setUpClass(cls):
        """This method is used to prepare the test fixture
        This method is used to prepare the test fixture.
        It ensures the file_storage module is ready for testing.
        """
        cls.fs_f = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_pep8_conformance_file_storage(self):
        """This method checks for PEP8 conformance in the file_storage module.
        It ensures the file_storage module conforms to PEP8 standards.
        """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_file_storage(self):
        """This method checks for PEP8 conformance in the test_file_storage.py file.
        It ensures the test_file_storage.py file conforms to PEP8 standards.
        """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\test_file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
        
    def test_file_storage_module_docstring(self):
        """This method tests for the presence of a docstring in the file_storage module.
        It ensures the file_storage module has a docstring.
        """
        self.assertIsNot(models.engine.file_storage.__doc__, None,
                         "file_storage.py needs a docstring")
        self.assertTrue(len(models.engine.file_storage.__doc__) >= 1,
                        "file_storage.py needs a docstring")
        
    def test_file_storage_class_docstring(self):
        """This method tests for the presence of a docstring in the FileStorage class.
        It ensures the FileStorage class has a docstring.
        """
        self.assertIsNot(FileStorage.__doc__, None,
                         "FileStorage class needs a docstring")
        self.assertTrue(len(FileStorage.__doc__) >= 1,
                        "FileStorage class needs a docstring")
        
    def test_fs_func_docstrings(self):
        """This method tests for the presence of docstrings in FileStorage methods.
        It ensures the FileStorage methods have docstrings.
        """
        for func in self.fs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))
            
class TestFileStorage(unittest.TestCase):
    """This class contains test cases for the FileStorage class
    This class contains test cases for the FileStorage class in the file_storage module.
    It includes test cases for the FileStorage class methods.
    """
    @unittest.skipIf(models.os.getenv(HBNB_TYPE_STORAGE) == 'db' == 'db', "not testing file storage")
    def test_all_returns_dict(self):
        """This method tests that all returns the FileStorage.__objects attr.
        It ensures that the all method returns the FileStorage.__objects attribute.
        """
        storage = FileStorage()
        new_dict = storage.all()
        self.assertEqual(type(new_dict), dict)
        self.assertIs(new_dict, storage._FileStorage__objects)

    @unittest.skipIf(models.os.getenv(HBNB_TYPE_STORAGE) == 'db' == 'db', "not testing file storage")
    def test_new(self):
        """This method tests that new adds an object to the FileStorage.__objects attr.
        It ensures that the new method adds an object to the FileStorage.__objects attribute.
        """
        storage = FileStorage()
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}
        test_dict = {}
        for key, value in classes.items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = instance.__class__.__name__ + "." + instance.id
                storage.new(instance)
                test_dict[instance_key] = instance
                self.assertEqual(test_dict, storage._FileStorage__objects)
        FileStorage._FileStorage__objects = save

    @unittest.skipIf(models.os.getenv(HBNB_TYPE_STORAGE) == 'db' == 'db', "not testing file storage")
    def test_save(self):
        """This method tests that save properly saves objects to file.json.
        It ensures that the save method properly saves objects to the file.json file.
        """
        storage = FileStorage()
        new_dict = {}
        for key, value in classes.items():
            instance = value()
            instance_key = instance.__class__.__name__ + "." + instance.id
            new_dict[instance_key] = instance
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = new_dict
        storage.save()
        FileStorage._FileStorage__objects = save
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        string = json.dumps(new_dict)
        with open("file.json", "r") as f:
            js = f.read()
        self.assertEqual(json.loads(string), json.loads(js))
        