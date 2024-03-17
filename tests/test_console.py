#!/usr/bin/python3
"""
Contains the class TestConsoleDocs
"""


import unittest
from unittest.mock import patch
from io import StringIO
import os
import pep8
import console
from console import HBNBCommand


class TestConsoleDocs(unittest.TestCase):
    """Class for testing documentation of the console"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.console_help = os.popen('hbnb help').read()
        cls.all_help = os.popen('help').read()

    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py', 'tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """Test that test_console.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py', 'tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docstring(self):
        """Test docstring for console and test_console.py"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.__doc__)

    def test_help(self):
        """Test help command"""
        self.assertEqual(self.console_help, self.all_help)
