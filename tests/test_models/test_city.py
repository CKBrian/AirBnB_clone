#!/usr/bin/env python3
"""defines test_base_model modules with testcases for base_model module"""
from unittest import TestCase
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from io import StringIO
from datetime import datetime
import unittest
import sys


class TestCity(TestCase):
    def test_instantiation(self):
        """Tests for object instantiation"""
        city1 = City()
        self.assertIsInstance(city1, City)

        self.assertEqual(type(city1.state_id), str)

        self.assertEqual(type(city1.name), str)

        self.assertIsInstance(city1.created_at, datetime)

        self.assertIsInstance(city1.updated_at, datetime)

        self.assertIsInstance(city1.id, str)

    def test_save(self):
        """tests for save method"""
        city1 = City()
        obj_id1 = "City.{}".format(city1.id)
        city1.save()
        obj_saved = city1.to_dict()
        storage = FileStorage()
        storage.reload()
        city2 = City(**obj_saved)
        obj_reloaded = city2.to_dict()
        self.assertEqual(obj_saved, obj_reloaded)

    def test__str__(self):
        """tests for __str__ method"""
        c1 = City()
        dict_str = c1.to_dict()
        c2 = City(**dict_str)

        self.assertEqual(str(c2), str(c1))

    def test_to_dict(self):
        """tests for to_dict method"""
        c1 = City()
        dict_str = c1.to_dict()
        c2 = City(**dict_str)

        self.assertEqual(c2.to_dict(), c1.to_dict())


if __name__ == "__main__":
    unittest.main()
