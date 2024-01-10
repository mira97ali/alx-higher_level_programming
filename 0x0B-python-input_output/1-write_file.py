#!/usr/bin/python3
"""Write to a file"""

def write_file(filename="", text=""):
    """write a file"""
    with open(filename, mode="w", encoding="utf-8") as file:
        characters_written = file.write(text)
        return characters_written
