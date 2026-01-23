#!/usr/bin/python3
"""
Prints text with two newlines after each '.', '?', or ':'
"""


def text_indentation(text=""):
    """Prints text with two newlines after each '.', '?', or ':'"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace(".", ".\n\n")
    text = text.replace("?", "?\n\n")
    text = text.replace(":", ":\n\n")
    print(text, end="")
