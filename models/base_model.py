#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models

"""
Class Base
"""


class BaseModel():
    """
    defines all common attributes/methods for other classes
    """
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Return a string with info about Model object"""
        return ("[{}] ({})  {}".
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ Updates the public instance attribute
        updated_at with the current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
        of __dict__ of the instance """
        dictionary = {}

        for k, v in self.__dict__.items():
            if isinstance(v, (datetime, )):
                dictionary[k] = v.isoformat()
            else:
                dictionary[k] = v
        return dictionary
