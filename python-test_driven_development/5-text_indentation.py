#!/usr/bin/python3
"""Module for text indentation."""


def text_indentation(text):
    """Print text with a newline after each '.', '?', and ':' character."""
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    n = len(text)
    last_char = ''
    while i < n:
        print(text[i], end="")
        last_char = text[i]
        if text[i] in ".?:":
            print()
            last_char = '\n'
            i += 1
            # Skip all spaces after punctuation
            while i < n and text[i] == ' ':
                i += 1
            continue
        i += 1
    if last_char != '\n':
        print()
