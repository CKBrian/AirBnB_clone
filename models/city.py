#!/usr/bin/env python3
"""defines city module that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """
        inherits from BaseModel

        Attributes:
            name (str): city name
            state_id(str): state id as State.id

    """
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """initializes City class"""
        super().__init__(**kwargs)
