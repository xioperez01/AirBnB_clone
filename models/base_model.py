#!/usr/bin/python3
"""
Module BaseModel
Defines all common attributes/methods
for other classes
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """
    defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """ Constructor """
        if kwargs:
            for k, v in kwargs.items():
                if "__class__" == k:
                    pass
                elif "created_at" == k:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == k:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Return a string with info about Model object"""
        return ("[{}] ({})  {}".
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ Updates the public instance attribute
        updated_at with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
        of __dict__ of the instance """
        dictionary = {}
        dictionary["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if isinstance(v, (datetime, )):
                dictionary[k] = v.isoformat()
            else:
                dictionary[k] = v
        return dictionary
