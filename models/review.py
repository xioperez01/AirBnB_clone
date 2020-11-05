#!/usr/bin/python3
""" Module Review """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Classes inherit from BaseModel """
    place_id = ""
    user_id = ""
    text = ""
