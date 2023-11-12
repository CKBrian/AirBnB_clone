#!/usr/bin/env python3
"""defines test_base_model modules with testcases for base_model module"""
import unittest
from unittest import TestCase
from models.base_model import BaseModel


class TestBaseModel(TestCase):
    def test_instantiation(self):
        """Tests for object instantiation"""
        model1 = BaseModel()
        self.assertIsInstance(model1, BaseModel)
        model2 = BaseModel()
        dict_obj = model2.to_dict()
        self.assertNotEqual(model1.id, model2.id)
        self.assertEqual(dict_obj['__class__'], 'BaseModel')
        mod3 = BaseModel(**dict_obj)
        self.assertEqual(mod3.to_dict(), dict_obj)

    def test___str__(self):
        """tests for __str__ method"""
        pass

    def test_save(self):
        """tests for save method"""
        pass

    def test_to_dict(self):
        """tests for to_dict method"""
        pass


if __name__ == "__main__":
    unittest.main()
