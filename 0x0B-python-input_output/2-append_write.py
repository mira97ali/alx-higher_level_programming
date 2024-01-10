#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """Append a text to a file"""
    with open(filename, mode="a", encoding="utf-8") as file:
        characters_added = file.write(text)
        return characters_added
