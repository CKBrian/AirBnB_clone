#!/usr/bin/env python3
"""defines test_base_model modules with testcases for base_model module"""
from unittest import TestCase
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from io import StringIO
import unittest
import sys


class TestUser(TestCase):
    def test_instantiation(self):
        """Tests for object instantiation"""
        user1 = User()

        self.assertEqual(type(user1.email), str)

        self.assertEqual(type(user1.password), str)

        self.assertEqual(type(user1.first_name), str)

        self.assertEqual(type(user1.last_name), str)

        self.assertIsInstance(user1.created_at, datetime)

        self.assertIsInstance(user1.updated_at, datetime)

        self.assertIsInstance(user1.id, str)
        self.assertIsInstance(user1, User)
        user2 = User()
        dict_obj = user2.to_dict()
        self.assertNotEqual(user1.id, user2.id)
        self.assertEqual(dict_obj['__class__'], 'User')
        usr3 = User(**dict_obj)
        self.assertEqual(usr3.to_dict(), dict_obj)

    def test_save(self):
        """tests for save method"""
        user1 = User()
        obj_id1 = "User.{}".format(user1.id)
        user1.save()
        obj_saved = user1.to_dict()
        storage = FileStorage()
        storage.reload()
        user2 = User(**obj_saved)
        obj_reloaded = user2.to_dict()
        self.assertEqual(obj_saved, obj_reloaded)

    def test__str__(self):
        """tests for __str__ method"""
        output = StringIO()
        sys.stdout = output

        m1 = User()
        print(m1)
        dict_obj = m1.to_dict()

        sys.stdout = sys.__stdout__
        res1 = output.getvalue()

        output = StringIO()
        sys.stdout = output

        m2 = User(**dict_obj)
        print(m2)

        sys.stdout = sys.__stdout__
        res2 = output.getvalue()
        self.assertEqual(res1, res2)

    def test_to_dict(self):
        """tests for to_dict method"""
        pass


if __name__ == "__main__":
    unittest.main()
