#!/usr/bin/python3
"""Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """Create object"""
    with open(filename, mode="r", encoding="UTF-8") as file:
        return json.load(file)
