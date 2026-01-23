#!/usr/bin/python3
"""Defines a text indentation function."""


def text_indentation(text):
    """Print text with a new line after each '.', '?', and ':' character."""
    if type(text) is not str:
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print()  # fixed: only one newline now
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
