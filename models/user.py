#!/usr/bin/python3
""" Module User """
from models.base_model import BaseModel


class User(BaseModel):
    """ Classes inherit from BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
