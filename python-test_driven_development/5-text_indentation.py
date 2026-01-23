#!/usr/bin/python3
"""
Function that prints a text with 2 new lines
after each of these characters: ., ? and :.
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines after
    each of these characters: ., ? and :.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace(".", ".\n\n")
    text = text.replace("?", "?\n\n")
    text = text.replace(":", ":\n\n")
    print(text, end="")
