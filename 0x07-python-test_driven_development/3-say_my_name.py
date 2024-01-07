#!/usr/bin/python3
"""Say my name, Heisenberg"""


def say_my_name(first_name, last_name=""):
    """function that prints your name"""
    if not isinstance(first_name, str):
        raise ValueError("first_name must be a string")

    if not isinstance(last_name, str):
        raise ValueError("last_name must be a string")

    return " ".join(
        item
        for item in (
            "My name is",
            first_name.strip(),
            last_name.strip()
        )
        if item
    )
