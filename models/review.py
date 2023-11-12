#!/usr/bin/env python3
"""defines review module that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
        inherits from BaseModel

        Attributes:
            place_id (str): place id as Place.id
            user_id (str): user id as User.id
            text (str): review text

    """
    user_id = ""
    text = ""
    place_id = ""

    def __init__(self, *args, **kwargs):
        """initializes Review class"""
        super().__init__(**kwargs)
