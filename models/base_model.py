#!/usr/bin/env python3
"""defines a base_model module"""
from datetime import datetime
import json
import uuid


class BaseModel():
    """
        defines all common attributes/methods for other classes:
    """
    def __init__(self, *args, **kwargs):
        """
            Initializes BaseModel class
            Args:
                kwargs(:obj: `dict`): dictionary of BaseModel class attributes
                created_at (:obj: `datetime`): stores date & time a
                                               new instance is created
                updated_at (:obj: `datetime`): stores date & time an
                                               instance is updated
        """
        from models import storage
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "updated_at" or key == "created_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
                elif key == "id":
                    self.id = value
                else:
                    setattr(self, key, value)

    def __str__(self):
        """formats the output string when print is called"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
            updates public instance attribute
            updated_at with the current datetime
            Args:
                dict_keys (:obj: `list`): list of BaseModel instances'
                                          dictionary keys
                objects (:obj: `dict`): nested dictionary of BaseModel objects
        """
        from models import storage
        self.updated_at = datetime.now()
        dict_keys = list(storage.__class__._FileStorage__objects.keys())
        objects = storage.__class__._FileStorage__objects
        for key, value in self.__dict__.items():
            if key not in objects[dict_keys[-1]]:
                objects[dict_keys[-1]][key] = value
        storage.save()

    def to_dict(self):
        """
            returns a dictionary containing all keys/values
            of __dict__ of the instance

            Args:
                s_dict (:obj: `dict`): copy of a BaseModel __dict__ attribute
        """
        s_dict = self.__dict__.copy()
        s_dict['__class__'] = self.__class__.__name__
        s_dict['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        s_dict['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return s_dict
