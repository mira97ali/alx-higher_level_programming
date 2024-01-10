#!/usr/bin/python3
"""Class to JSON"""


def class_to_json(obj):
    """Class to JSON"""
    obj_dict = obj.__dict__.copy()
    for key in obj_dict.keys():
        if key.startswith("_"):
            new_key = "{}{}".format(obj.__class__.__name__, key)
            obj_dict[new_key] = obj_dict.pop(key)
    return obj_dict
