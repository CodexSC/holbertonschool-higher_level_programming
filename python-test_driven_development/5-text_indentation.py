#!/usr/bin/python3
"""Module for text indentation."""


def text_indentation(text):
    """Print text with a newline after each '.', '?', and ':' character."""
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    n = len(text)
    while i < n:
        print(text[i], end="")
        if text[i] in ".?:":
            print()
            i += 1
            # Skip all spaces after punctuation
            while i < n and text[i] == ' ':
                i += 1
            continue
        i += 1
