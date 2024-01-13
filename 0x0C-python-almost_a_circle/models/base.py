#!/usr/bin/python3
"""Base class"""
import json


class Base:
    """Creates the base class of shapes"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise NotImplementedError(
                f"Implement {cls.__name__} first")
        dummy_instance.update(**dictionary)
        return dummy_instance

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs]
            ))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by json_string"""
        if not json_string:
            return []
        return json.loads(json_string)
