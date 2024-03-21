#!/usr/bin/python3

"""
This module contains test cases for the Review class in the models module.
The test cases ensure the Review class is working as expected.
It also ensures the attributes and methods
of the Review class are working as expected.
"""

import unittest
import datetime
from models.review import Review
from models.base_model import BaseModel
import inspect
import pep8
from models import review
import models

Review = Review


class TestReview(unittest.TestCase):
    """
    This class contains test cases for the Review class.
    It includes test cases for the attributes
    and methods of the Review class.
    The test cases ensure the Review class is working as expected.
    """

    def setUpClass(cls):
        """
        This method is used to prepare the test fixture.
        It ensures the Review class is ready for testing.
        The method is called before any
        test case of the TestReview class is run.
        """
        cls.review_f = inspect.getmembers(Review, inspect.isfunction)

    def test_pep8_conformance_review(self):
        """
        This method checks for PEP8 conformance in the Review class.
        It ensures the Review class conforms to PEP8 standards.
        """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_review(self):
        """
        This method checks for PEP8 conformance in the test_review.py file.
        It ensures the test_review.py file conforms to PEP8 standards.
        """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_review_module_docstring(self):
        """
        This method tests for the presence
        of a docstring in the review.py module.
        It ensures the review.py module has a docstring.
        """
        self.assertIsNot(review.__doc__, None,
                         "review.py needs a docstring")
        self.assertTrue(len(review.__doc__) >= 1,
                        "review.py needs a docstring")

    def test_review_class_docstring(self):
        """
        This method tests for the presence of a docstring in the Review class.
        It ensures the Review class has a docstring.
        """
        self.assertIsNot(Review.__doc__, None,
                         "Review class needs a docstring")
        self.assertTrue(len(Review.__doc__) >= 1,
                        "Review class needs a docstring")

    def test_review_func_docstrings(self):
        """
        This method tests for the presence of docstrings in Review methods.
        It ensures the methods of the Review class have docstrings.
        """
        for func in self.review_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

    def test_is_subclass(self):
        """
        Test if Review is a subclass of BaseModel.
        """
        review = Review()
        self.assertTrue(issubclass(review.__class__, BaseModel), True)

    def test_place_id_attr(self):
        """
        This method tests if Review has an
        attribute place_id, and it's an empty string.
        It ensures the Review class has
        an attribute place_id, and it's an empty string by default.
        The test passes if the attribute is present and it's an empty string.
        """
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        if models.storage_t == 'db':
            self.assertEqual(review.place_id, None)
        else:
            self.assertEqual(review.place_id, "")

    def test_user_id_attr(self):
        """
        This method tests if Review has an
        attribute user_id, and it's an empty string.
        It ensures the Review class has
        an attribute user_id, and it's an empty string by default.
        The test passes if the attribute
        is present and it's an empty string.
        """
        review = Review()
        self.assertTrue(hasattr(review, "user_id"))
        if models.storage_t == 'db':
            self.assertEqual(review.user_id, None)
        else:
            self.assertEqual(review.user_id, "")

    def test_text_attr(self):
        """
        This method tests if Review
        has an attribute text, and it's an empty string.
        It ensures the Review class has
        an attribute text, and it's an empty string by default.
        The test passes if the attribute
        is present and it's an empty string.
        """
        review = Review()
        self.assertTrue(hasattr(review, "text"))
        if models.storage_t == 'db':
            self.assertEqual(review.text, None)
        else:
            self.assertEqual(review.text, "")

    def test_to_dict_creates_dict(self):
        """
        This method tests if the to_dict method creates a dictionary.
        It ensures the to_dict method creates
        a dictionary representation of the Review instance.
        The test passes if the output is a dictionary.
        """
        review = Review()
        new_dict = review.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertTrue(type(new_dict['created_at']) is str)
        self.assertTrue(type(new_dict['updated_at']) is str)

    def test_to_dict_values(self):
        """
        This method tests if the to_dict method
        creates a dictionary with proper key/values.
        It ensures the to_dict method creates
        a dictionary with the expected key/values.
        The test passes if the key/values are as expected.
        """
        review = Review()
        new_dict = review.to_dict()
        self.assertEqual(new_dict['__class__'], 'Review')
        self.assertEqual(type(new_dict['created_at']), str)
        self.assertEqual(type(new_dict['updated_at']), str)

    def test_str(self):
        """
        This method tests the __str__ method of the Review class.
        It ensures the __str__ method of the
        Review class prints the expected string.
        The test passes if the output is as expected.
        """
        review = Review()
        string = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(string, str(review))