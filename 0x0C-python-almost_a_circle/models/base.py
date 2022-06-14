#!/usr/bin/python3
"""
...
"""
from fileinput import filename
import json

class Base:
    """
    ...
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        ...
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        ...
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        if list_objs is None or list_objs == []:
            json_s = "[]"
        else:
            json_s = cls.to_json_string([element.to_dictionary() for element in list_objs])
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as file:
            file.write(json_s)

    @staticmethod
    def from_json_string(json_string):
        """
        ...
        """
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        ...
        """
        