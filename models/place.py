#!/usr/bin/env python3
"""defines place module that inherits from BaseModel"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
        inherits from BaseModel

        Attributes:
            name (str): place name
            city_id (str): city id as City.id
            user_id (str): user id as User.id
            description (str): place description
            number_rooms (int): number of rooms
            number_bathrooms (int): number of bathrooms
            max_guest (int): number of guests
            price_by_night (int): room price by night
            latitude (float): latitude of the place
            longitude (float): longitude of the place
            amenity_ids (:obj: `list`): list of Amenity.id strings

    """
    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """initializes Place class"""
        super().__init__(**kwargs)
