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
