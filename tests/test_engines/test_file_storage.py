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
    @classmethod
    def setUpClass(cls):
        print("Welcome to FileStorage unittests")

        file_path = os.path.join(os.path.dirname(__file__), "file.json")
        path = file_path.split("tests/test_engines/")
        file_path = path[0] + path[1]
        if os.path.exists(file_path):
            os.remove(file_path)

    def test_instantiation(self):
        """tests for instantiation"""
        storage = FileStorage()

        self.assertEqual({}, storage.all())

        self.assertIsInstance(storage1, FileStorage)

        self.assertEqual(type(storage._FileStorage__file_path), str)

        self.assertEqual(type(storage._FileStorage__objects), dict)

    def test_all(self):
        """Tests for all method"""
        storage1 = FileStorage()
        storage1.reload()
        res = storage1.all()
        self.assertEqual(type(res), dict)
        self.assertIs(storage1._FileStorage__objects, res)

        storage2 = FileStorage()
        storage2.reload()
        dict_obj = storage2.all()
        self.assertEqual(dict_obj, storage2._FileStorage__objects)

    @classmethod
    def tearDownClass(cls):
        print("Exiting FileStorage unittests")

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
