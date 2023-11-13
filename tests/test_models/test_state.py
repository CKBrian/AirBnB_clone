#!/usr/bin/env python3
"""defines test_base_model modules with testcases for base_model module"""
from unittest import TestCase
from models.base_model import BaseModel
from models.state import State
from models.engine.file_storage import FileStorage
from io import StringIO
import unittest
import sys


class TestState(TestCase):
    def test_instantiation(self):
        """Tests for object instantiation"""
        state1 = State()
        self.assertIsInstance(state1, State)
        state2 = State()
        dict_obj = state2.to_dict()
        self.assertNotEqual(state1.id, state2.id)
        self.assertEqual(dict_obj['__class__'], 'State')
        mod3 = State(**dict_obj)
        self.assertEqual(mod3.to_dict(), dict_obj)

    def test_save(self):
        """tests for save method"""
        state1 = State()
        obj_id1 = "State.{}".format(state1.id)
        state1.save()
        obj_saved = state1.to_dict()
        storage = FileStorage()
        storage.reload()
        state2 = State(**obj_saved)
        obj_reloaded = state2.to_dict()
        self.assertEqual(obj_saved, obj_reloaded)

    def test__str__(self):
        """tests for __str__ method"""
        output = StringIO()
        sys.stdout = output

        m1 = State()
        print(m1)
        dict_obj = m1.to_dict()

        sys.stdout = sys.__stdout__
        res1 = output.getvalue()

        output = StringIO()
        sys.stdout = output

        m2 = State(**dict_obj)
        print(m2)

        sys.stdout = sys.__stdout__
        res2 = output.getvalue()
        self.assertEqual(res1, res2)

    def test_to_dict(self):
        """tests for to_dict method"""
        pass


if __name__ == "__main__":
    unittest.main()
