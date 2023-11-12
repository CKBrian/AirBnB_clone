#!/usr/bin/env python3
"""defines amenity module that inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
        inherits from BaseModel

        Attributes:
            name (str): amenity name

    """
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity class"""
        super().__init__(**kwargs)
