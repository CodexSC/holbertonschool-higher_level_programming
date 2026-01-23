#!/usr/bin/python3
"""Module for text indentation."""


def text_indentation(text):
    """Print text with a newline after each '.', '?', and ':' character."""
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    n = len(text)
    last_was_newline = False
    while i < n:
        c = text[i]
        print(c, end="")
        if c in ".?:":
            print()
            last_was_newline = True
            i += 1
            # Skip all spaces after punctuation
            while i < n and text[i] == ' ':
                i += 1
            continue
        else:
            last_was_newline = False
        i += 1
    if not last_was_newline:
        print()
