#!/usr/bin/python3
"""Print text with a new line after each '.', '?', and ':' character."""


def text_indentation(text):
    """Print text with a new line after each '.', '?', and ':' character."""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    print(text, end="")
