#!/usr/bin/env python3
"""
    defines file_storage module with a class FileStorage that serializes
    instances to a JSON file and deserializes JSON file to instances

"""
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from datetime import datetime
import json
import os


class FileStorage():
    """
        defines a class FileStorage that serializes
        instances to a JSON file and deserializes JSON file to instances

        Attributes:
        __file_path (str): Path to the JSON file
        __objects (:obj: `dict`): Stores all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return type(self).__objects

    def new(self, obj):
        """
            sets in __objects the obj with key <obj class name>.id
            Args:
                obj (:obj: `class obj`): class object
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        value = obj.to_dict()
        type(self).__objects[key] = value

    def save(self):
        """serializes objects to the JSON file"""
        objects = type(self).__objects
        objects_dict = {}
        for key, value in objects.items():
            if isinstance(value, BaseModel):
                objects_dict[key] = value.to_dict()
            elif isinstance(value, User):
                objects_dict[key] = value.to_dict()
            elif isinstance(value, Place):
                objects_dict[key] = value.to_dict()
            elif isinstance(value, State):
                objects_dict[key] = value.to_dict()
            elif isinstance(value, City):
                objects_dict[key] = value.to_dict()
            elif isinstance(value, Amenity):
                objects_dict[key] = value.to_dict()
            elif isinstance(value, Review):
                objects_dict[key] = value.to_dict()
            else:
                objects_dict[key] = value

        with open(type(self).__file_path, "w") as s_file:
            json.dump(objects_dict, s_file)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists otherwise, does nothing
        """
        objects = {}
        try:
            with open(type(self).__file_path, "r") as s_file:
                objects = json.load(s_file)
                for key, value in objects.items():
                    class_name = key.split('.')
                    if class_name[0] == "BaseModel":
                        reloaded_obj = BaseModel(**value)
                    elif class_name[0] == "User":
                        reloaded_obj = User(**value)
                    elif class_name[0] == "Place":
                        reloaded_obj = Place(**value)
                    elif class_name[0] == "State":
                        reloaded_obj = State(**value)
                    elif class_name[0] == "City":
                        reloaded_obj = City(**value)
                    elif class_name[0] == "Amenity":
                        reloaded_obj = Amenity(**value)
                    elif class_name[0] == "Review":
                        reloaded_obj = Review(**value)
                    type(self).__objects[key] = reloaded_obj
        except FileNotFoundError:
            pass
