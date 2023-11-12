#!/usr/bin/env python3
"""defines user module that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """
        inherits from BaseModel

        Attributes:
            email (str): user email
            password (str): user password
            first_name (str): user first_name
            last_name (str): user last_name

    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes User class"""
        super().__init__(**kwargs)
