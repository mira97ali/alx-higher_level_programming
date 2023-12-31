#!/usr/bin/python3
ROMAN_NUMERALS = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


def roman_to_int(roman_string):
    result = 0
    if isinstance(roman_string, str):
        prev_value = 0
        for char in reversed(roman_string):
            value = ROMAN_NUMERALS[char]
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value
    return result
