#!/usr/bin/env python3
"""defines test_base_model modules with testcases for base_model module"""
from unittest import TestCase
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from io import StringIO
import unittest
import sys
import os


class TestFileStorage(TestCase):
    def test_all(self):
        """Tests for all method"""

        file_path = os.path.join(os.path.dirname(__file__), "file.json")
        path = file_path.split("tests/test_models/")
        file_path = path[0] + path[1]
        if os.path.exists(file_path):
            os.remove(file_path)
        storage1 = FileStorage()
        self.assertIsInstance(storage1, FileStorage)
        storage1.reload()
        res = storage1.all()
        # self.assertEqual(None, res)

        storage2 = FileStorage()
        storage2.reload()
        dict_obj = storage2.all()
        self.assertEqual(dict_obj, storage2._FileStorage__objects)

    def test_new(self):
        """tests new method"""
        mod = BaseModel()
        res = mod.to_dict()
        obj_id = "BaseModel.{}".format(mod.id)
        storage = FileStorage()
        storage.new(mod)
        res2 = storage._FileStorage__objects[obj_id]
        # self.assertEqual(res, res2)

    def test_save(self):
        """tests for save and reload file storage methods"""
        model1 = BaseModel()
        obj_id1 = "BaseModel.{}".format(model1.id)
        model1.save()
        obj_saved = model1.to_dict()
        storage = FileStorage()
        storage.reload()
        model2 = BaseModel(**obj_saved)
        obj_reloaded = model2.to_dict()
        self.assertEqual(obj_saved, obj_reloaded)


if __name__ == "__main__":
    unittest.main()
