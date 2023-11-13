#!/usr/bin/env python3
"""defines test_base_model modules with testcases for base_model module"""
from unittest import TestCase
from models.base_model import BaseModel
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from io import StringIO
import unittest
import sys


class TestAmenity(TestCase):
    def test_instantiation(self):
        """Tests for object instantiation"""
        amenity1 = Amenity()
        self.assertIsInstance(amenity1, Amenity)
        amenity2 = Amenity()
        dict_obj = amenity2.to_dict()
        self.assertNotEqual(amenity1.id, amenity2.id)
        self.assertEqual(dict_obj['__class__'], 'Amenity')
        mod3 = Amenity(**dict_obj)
        self.assertEqual(mod3.to_dict(), dict_obj)

    def test_save(self):
        """tests for save method"""
        amenity1 = Amenity()
        obj_id1 = "Amenity.{}".format(amenity1.id)
        amenity1.save()
        obj_saved = amenity1.to_dict()
        storage = FileStorage()
        storage.reload()
        amenity2 = Amenity(**obj_saved)
        obj_reloaded = amenity2.to_dict()
        self.assertEqual(obj_saved, obj_reloaded)

    def test__str__(self):
        """tests for __str__ method"""
        output = StringIO()
        sys.stdout = output

        m1 = Amenity()
        print(m1)
        dict_obj = m1.to_dict()

        sys.stdout = sys.__stdout__
        res1 = output.getvalue()

        output = StringIO()
        sys.stdout = output

        m2 = Amenity(**dict_obj)
        print(m2)

        sys.stdout = sys.__stdout__
        res2 = output.getvalue()
        self.assertEqual(res1, res2)

    def test_to_dict(self):
        """tests for to_dict method"""
        pass


if __name__ == "__main__":
    unittest.main()
