#!/usr/bin/python3
import json
from models.base_model import BaseModel
""" Class File_storage """


class FileStorage():
    """ Serializes instances to a JSON file and
    deserializes JSON file to instances """

    # Private class attributes:
    __file_path = "file.json"
    __objects = {}

    # Public instance methods
    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the new obj with
        key <obj class name>.id """
        if obj:
            k = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[k] = obj

    def save(self):
        """ Serializes __objects to the JSON file
        (path: __file_path)"""
        dictionary = {}
        for k, obj in self.__objects.items():
            dictionary[k] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(dictionary, f)

    def reload(self):
        """ deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists"""
        try:
            with open(FileStorage.__file_path) as fp:
                data = json.load(fp)
            for key, value in data.items():
                eval(key.split(".")[0] + '(**value)')
        except FileNotFoundError:
            pass
        
