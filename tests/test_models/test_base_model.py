#!/usr/bin/env python3
"""defines test_base_model modules with testcases for base_model module"""
from unittest import TestCase
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from io import StringIO
import unittest
import sys


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

    def test_save(self):
        """tests for save method"""
        model1 = BaseModel()
        obj_id1 = "BaseModel.{}".format(model1.id)
        model1.save()
        obj_saved = model1.to_dict()
        storage = FileStorage()
        storage.reload()
        model2 = BaseModel(**obj_saved)
        obj_reloaded = model2.to_dict()
        self.assertEqual(obj_saved, obj_reloaded)

    def test__str__(self):
        """tests for __str__ method"""
        output = StringIO()
        sys.stdout = output

        m1 = BaseModel()
        print(m1)
        dict_obj = m1.to_dict()

        sys.stdout = sys.__stdout__
        res1 = output.getvalue()

        output = StringIO()
        sys.stdout = output

        m2 = BaseModel(**dict_obj)
        print(m2)

        sys.stdout = sys.__stdout__
        res2 = output.getvalue()
        self.assertEqual(res1, res2)

    def test_to_dict(self):
        """tests for to_dict method"""
        pass


if __name__ == "__main__":
    unittest.main()
