#!/usr/bin/python3
"""Class to JSON"""


def class_to_json(obj):
    """Class to JSON"""
    result = {}
    for key, value in obj.__dict__.items():
        if not key.startswith("_"):
            result[key] = value
    return result
