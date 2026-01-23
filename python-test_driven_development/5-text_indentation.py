#!/usr/bin/python3
"""Module for text indentation."""

def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':' characters."""
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace(".", ".\n\n")
    text = text.replace("?", "?\n\n")
    text = text.replace(":", ":\n\n")
    text = text.strip().replace("\n\n ", "\n\n")
    lines = text.split("\n")
    indented_text = ""
    for line in lines:
        indented_text += line.strip() + "\n"
    return indented_text
