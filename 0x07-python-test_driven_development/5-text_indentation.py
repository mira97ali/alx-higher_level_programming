#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """
    Print a text with 2 new lines after each '.', '?', and ':' characters.

    Args:
    - text (str): The input text.

    Raises:
    - TypeError: If text is not a string.

    Returns:
    - None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_chars = ['.', '?', ':']
    current_line = ''

    for char in text:
        current_line += char

        if char in punctuation_chars:
            print(current_line.strip())
            print()
            current_line = ''

    if current_line.strip():
        print(current_line.strip())
