#!/usr/bin/env python3
"""defines state module that inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """
        inherits from BaseModel

        Attributes:
            name (str): state name

    """
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes State class"""
        super().__init__(**kwargs)
