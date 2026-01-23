#!/usr/bin/python3
"""Module for text indentation."""


def text_indentation(text=""):
    """Print text with two new lines after each of these characters: . ? :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace(".", ".\n\n")
    text = text.replace("?", "?\n\n")
    text = text.replace(":", ":\n\n")
    print(text, end="")
