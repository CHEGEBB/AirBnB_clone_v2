#!/usr/bin/python3
"""Unittest class for testing BaseModel class """
from models.base_model import BaseModel
import json
import os
import unittest
import datetime
from uuid import UUID


class TestBaseModel(unittest.TestCase):
    """
    each class is a unit test for basemodel
    """

    def __init__(self, *args, **kwargs):
        """
        Sets up each test
        """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """
        Resets __objects
        """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_default(self):
        """Test default """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """Test kwargs """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """test_kwargs_int """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_kwargs_one(self):
        """Test kwargs_one """
        m = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**m)

    def test_kwargs_none(self):
        """Test kwargs_none """
        m = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**m)

    def test_str(self):
        """Test __str__ method"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """Test to_dict() method"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_id(self):
        """Test id attribute """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_updated_at(self):
        """Test updated_date attribute """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    def test_created_at(self):
        """Test created_at attribute """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)
