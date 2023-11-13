#!/usr/bin/env python3
"""defines test_base_model modules with testcases for base_model module"""
from unittest import TestCase
from models.base_model import BaseModel
from models.place import Place
from models.engine.file_storage import FileStorage
from io import StringIO
import unittest
import sys


class TestPlace(TestCase):
    def test_instantiation(self):
        """Tests for object instantiation"""
        place1 = Place()
        self.assertIsInstance(place1, Place)
        place2 = Place()
        dict_obj = place2.to_dict()
        self.assertNotEqual(place1.id, place2.id)
        self.assertEqual(dict_obj['__class__'], 'Place')
        plc3 = Place(**dict_obj)
        self.assertEqual(plc3.to_dict(), dict_obj)

    def test_save(self):
        """tests for save method"""
        place1 = Place()
        obj_id1 = "Place.{}".format(place1.id)
        place1.save()
        obj_saved = place1.to_dict()
        storage = FileStorage()
        storage.reload()
        place2 = Place(**obj_saved)
        obj_reloaded = place2.to_dict()
        self.assertEqual(obj_saved, obj_reloaded)

    def test__str__(self):
        """tests for __str__ method"""
        output = StringIO()
        sys.stdout = output

        m1 = Place()
        print(m1)
        dict_obj = m1.to_dict()

        sys.stdout = sys.__stdout__
        res1 = output.getvalue()

        output = StringIO()
        sys.stdout = output

        m2 = Place(**dict_obj)
        print(m2)

        sys.stdout = sys.__stdout__
        res2 = output.getvalue()
        self.assertEqual(res1, res2)

    def test_to_dict(self):
        """tests for to_dict method"""
        pass


if __name__ == "__main__":
    unittest.main()
