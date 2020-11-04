#!/usr/bin/python3
"""Base Model Class Test Module"""
import unittest
from datetime import datetime
import uuid
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Tests BaseModel Class """

    def test_id(self):
        """ Check if id is correct """
        my_model = BaseModel()
        my_model_1 = BaseModel()

        # Check id type
        self.assertEqual(type(my_model.id), str)
        self.assertEqual(type(my_model_1.id), str)

        # Check unique id
        self.assertNotEqual(my_model.id, my_model_1.id)

        # Check id len
        self.assertEqual(len(my_model.id), 36)
        self.assertEqual(len(my_model_1.id), 36)

    def test_created_ad(self):
        """ Check if date is correct """
        my_model = BaseModel()
        my_model_1 = BaseModel()

        # Check created_ad type
        self.assertEqual(type(my_model.created_at), datetime)
        self.assertEqual(type(my_model_1.created_at), datetime)

        # Check Updated
        self.assertNotEqual(my_model.created_at, my_model.updated_at)
        self.assertNotEqual(my_model_1.created_at, my_model_1.updated_at)

    def test_updated_ad(self):
        """ Check if updated is correct """
        my_model = BaseModel()
        my_model_1 = BaseModel()

        # Check Type
        self.assertEqual(type(my_model.updated_at), datetime)
        self.assertEqual(type(my_model_1.updated_at), datetime)

    def test_str(self):
        """ Check if __str__ is correct """
        my_model = BaseModel()
        my_model_1 = BaseModel()

        # Check ouput

    def test_to_dict(self):
        """ Check if to_dict is correct """
        my_model = BaseModel()
        my_model_1 = BaseModel()

        # Check type
        self.assertEqual(type(my_model.to_dict()), dict)
        self.assertEqual(type(my_model_1.to_dict()), dict)
