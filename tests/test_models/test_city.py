#!/usr/bin/python3
"""test for amenity"""
from tests.test_models.test_base_model import TestBaseModel
from models.city import City


class TestCity(TestBaseModel):
    """TestCity class"""

    def __init__(self, *args, **kwargs):
        """Initialize"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """assert state_id is of type str"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """assert name is of type str"""
        new = self.value()
        self.assertEqual(type(new.name), str)
