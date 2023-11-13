#!/usr/bin/env python3
"""defines test_base_model modules with testcases for base_model module"""
from unittest import TestCase
from models.base_model import BaseModel
from models.review import Review
from models.engine.file_storage import FileStorage
from io import StringIO
import unittest
import sys


class TestReview(TestCase):
    def test_instantiation(self):
        """Tests for object instantiation"""
        review1 = Review()
        self.assertIsInstance(review1, Review)
        review2 = Review()
        dict_obj = review2.to_dict()
        self.assertNotEqual(review1.id, review2.id)
        self.assertEqual(dict_obj['__class__'], 'Review')
        revw3 = Review(**dict_obj)
        self.assertEqual(revw3.to_dict(), dict_obj)

    def test_save(self):
        """tests for save method"""
        review1 = Review()
        obj_id1 = "Review.{}".format(review1.id)
        review1.save()
        obj_saved = review1.to_dict()
        storage = FileStorage()
        storage.reload()
        review2 = Review(**obj_saved)
        obj_reloaded = review2.to_dict()
        self.assertEqual(obj_saved, obj_reloaded)

    def test__str__(self):
        """tests for __str__ method"""
        output = StringIO()
        sys.stdout = output

        m1 = Review()
        print(m1)
        dict_obj = m1.to_dict()

        sys.stdout = sys.__stdout__
        res1 = output.getvalue()

        output = StringIO()
        sys.stdout = output

        m2 = Review(**dict_obj)
        print(m2)

        sys.stdout = sys.__stdout__
        res2 = output.getvalue()
        self.assertEqual(res1, res2)

    def test_to_dict(self):
        """tests for to_dict method"""
        pass


if __name__ == "__main__":
    unittest.main()
