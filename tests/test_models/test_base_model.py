#!/usr/bin/python3

"""This module contains tests for the BaseModel class
TestBaseModelDocs: tests for the BaseModel class docstrings
TestBaseModel: tests for the BaseModel class
This is the test suite for the BaseModel class.
"""
from uuid import UUID
import json
import os
from datetime import datetime
import inspect
import models
import pep8 as pycodestyle
import time
import unittest
from unittest import mock
BaseModel = models.base_model.BaseModel
module_doc = models.base_model.__doc__

class TestBaseModelDocs(unittest.TestCase):
    """This class contains tests to check the
    documentation and style of BaseModel class
    It is a subclass of unittest.TestCase.
    What it does is to check the documentation
    and style of BaseModel class.
    """
    @classmethod
    def setUpClass(self):
        """Set up for docstring tests
        This method is used to set up the
        docstring tests for the BaseModel class.
        """
        self.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pep8_conformance(self):
        """Test that models/base_model.py conforms to PEP8.
        This method is used to test that the BaseModel class conforms to PEP8.
        """
        for path in ['models/base_model.py',
                     'tests/test_models/test_base_model.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Test for the existence of module docstring
        This method is used to test for the existence
        of module docstring in the BaseModel class.
        """
        self.assertIsNot(module_doc, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 1,
                        "base_model.py needs a docstring")

    def test_class_docstring(self):
        """Test for the BaseModel class docstring
        This method is used to test for the existence
        of docstring in the BaseModel class.
        """
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")

    def test_func_docstrings(self):
        """Test for the presence of docstrings in BaseModel methods
        This method is used to test for the presence of
        docstrings in the BaseModel methods.
        """
        for func in self.base_funcs:
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


class TestBaseModel(unittest.TestCase):
    """This class contains tests for the BaseModel class
    It is a subclass of unittest.TestCase.
    What it does is to test the BaseModel class.
    """
    def test_instantiation(self):
        """Test the instantiation of the BaseModel class
        This method is used to test the instantiation of
        the BaseModel class.
        """
        i = BaseModel()
        self.assertEqual(type(i), BaseModel)

    def test_id(self):
        """Test the id of the BaseModel class
        This method is used to test the id of the BaseModel class.
        """
        i = BaseModel()
        self.assertEqual(type(i.id), str)

    def test_created_at(self):
        """Test the created_at of the BaseModel class
        This method is used to test the created_at of the BaseModel class.
        """
        i = BaseModel()
        self.assertEqual(type(i.created_at), datetime)

    def test_updated_at(self):
        """Test the updated_at of the BaseModel class
        This method is used to test the updated_at of the BaseModel class.
        """
        i = BaseModel()
        self.assertEqual(type(i.updated_at), datetime)

    def test_save(self):
        """Test the save method of the BaseModel class
        This method is used to test the save method of the BaseModel class.
        """
        i = BaseModel()
        i.save()
        self.assertNotEqual(i.created_at, i.updated_at)

    def test_to_dict(self):
        """Test the to_dict method of the BaseModel class
        This method is used to test the to_dict method of the BaseModel class.
        """
        i = BaseModel()
        i_dict = i.to_dict()
        self.assertEqual(type(i_dict), dict)
        self.assertTrue('to_dict' in dir(i))
        self.assertTrue('__class__' in i_dict)
        self.assertTrue('created_at' in i_dict)
        self.assertTrue('updated_at' in i_dict)
        self.assertTrue('id' in i_dict)

    def test_str(self):
        """Test the __str__ method of the BaseModel class
        This method is used to test the __str__ method
        of the BaseModel class.
        """
        i = BaseModel()
        self.assertEqual(str(i), '[BaseModel] ({}) {}'.format(i.id, i.__dict__))

    def test_kwargs(self):
        """Test the kwargs of the BaseModel class
        This method is used to test the kwargs of the BaseModel class.
        """
        i = BaseModel()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Test the kwargs int of the BaseModel class
        This method is used to test the kwargs int of the BaseModel class.
        """
        i = BaseModel()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_kwargs_none(self):
        """Test the kwargs none of the BaseModel class
        This method is used to test the kwargs none of the BaseModel class.
        """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = BaseModel(**n)

    def test_kwargs_one(self):
        """Test the kwargs one of the BaseModel class
        This method is used to test the kwargs one of the BaseModel class.
        """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = BaseModel(**n)

    def test_datetime_attributes(self):
        """Test the datetime attributes of the BaseModel class
        This method is used to test the datetime attributes of the BaseModel class.
        """
        tic = datetime.now()
        inst1 = BaseModel()
        toc = datetime.now()
        self.assertTrue(tic <= inst1.created_at <= toc)
        time.sleep(1e-4)
        tic = datetime.now()
        inst2 = BaseModel()
        toc = datetime.now()
        self.assertTrue(tic <= inst2.created_at <= toc)
        self.assertEqual(inst1.created_at, inst1.updated_at)
        self.assertEqual(inst2.created_at, inst2.updated_at)
        self.assertNotEqual(inst1.created_at, inst2.created_at)
        self.assertNotEqual(inst1.updated_at, inst2.updated_at)

    def test_uuid(self):
        """Test the uuid of the BaseModel class
        This method is used to test the uuid of the BaseModel class.
        """
        inst1 = BaseModel()
        inst2 = BaseModel()
        for inst in [inst1, inst2]:
            uuid = inst.id
            self.assertEqual(type(uuid), str)
            self.assertEqual(len(uuid), 36)
            self.assertEqual(str(UUID(uuid)), uuid)

    def test_to_dict(self):
        """This method tests the to_dict method of the BaseModel class
        It is used to test the to_dict method of the BaseModel class.
        """
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        d = my_model.to_dict()
        expected_attrs = ["id",
                          "created_at",
                          "updated_at",
                          "name",
                          "my_number",
                          "__class__"]
        self.assertCountEqual(d.keys(), expected_attrs)
        self.assertEqual(d['__class__'], 'BaseModel')
        self.assertEqual(d['name'], "Holberton")
        self.assertEqual(d['my_number'], 89)

    def test_to_dict_values(self):
        """This method tests the to_dict method of the BaseModel class
        It is used to test the to_dict method of the BaseModel class.
        """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        bm = BaseModel()
        new_d = bm.to_dict()
        self.assertEqual(new_d["__class__"], "BaseModel")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], bm.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], bm.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        inst = BaseModel()
        string = "[BaseModel] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """This method tests the save method of the BaseModel class
        It is used to test the save method of the BaseModel class.
        This method also tests that the updated_at attribute is updated
        """
        inst = BaseModel()
        old_created_at = inst.created_at
        old_updated_at = inst.updated_at
        inst.save()
        new_created_at = inst.created_at
        new_updated_at = inst.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)
        self.assertTrue(mock_storage.new.called)
        self.assertTrue(mock_storage.save.called)
