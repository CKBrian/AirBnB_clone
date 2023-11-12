#!/usr/bin/env python3
"""defines test_base_model modules with testcases for base_model module"""
import unittest
from unittest import TestCase
from models.base_model import BaseModel


class TestBaseModel(TestCase):
    def test_instantiation(self):
        model1 = BaseModel()
        self.assertIsInstance(model1, BaseModel)
        model2 = BaseModel()
        dict_obj = model2.to_dict()
        self.assertNotEqual(model1.id, model2.id)
        self.assertEqual(dict_obj['__class__'], 'BaseModel')
        mod3 = BaseModel(**dict_obj)
        self.assertEqual(mod3.to_dict(), dict_obj)

    def test___str__(self):
        pass

    def test_save(self):
        pass

    def test_to_dict(self):
        pass


if __name__ == "__main__":
    unittest.main()
