#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Convert to JSON"""
        if type(attrs) is not list:
            return self.__dict__
        result = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                result[key] = value
        return result

    def reload_from_json(self, json):
        """Reload from JSON"""
        for key, value in json.items():
            setattr(self, key, value)
