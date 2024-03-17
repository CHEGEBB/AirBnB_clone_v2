#!/usr/bin/python3
"""test for amenity"""
from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity


class TestAmenity(TestBaseModel):
    """
    each class is a unit test for amenity
    """

    def __init__(self, *args, **kwargs):
        """Initialize"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """assert name is of type str"""
        new = self.value()
        self.assertEqual(type(new.name), str)
