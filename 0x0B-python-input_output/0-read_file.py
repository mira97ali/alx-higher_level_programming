#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """Read a file"""
    with open(filename, encoding="utf-8") as file:
        content = file.read()
        print(content)
