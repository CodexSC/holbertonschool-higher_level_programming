#!/usr/bin/python3
"""Print text with two new lines after each of these characters: ., ? and :."""


def text_indentation(text):
    """Print text with two new lines after each of these characters: ., ? and :."""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    print(text, end="")
