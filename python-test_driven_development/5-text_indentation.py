#!/usr/bin/python3
"""Defines a text indentation function."""


def text_indentation(text):
    """Print text with a new line after each '.', '?', and ':' character."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    n = len(text)

    while i < n:
        # skip leading spaces
        while i < n and text[i] == " ":
            i += 1

        if i >= n:
            break

        # print characters until punctuation
        while i < n and text[i] not in ".?:":
            print(text[i], end="")
            i += 1

        # print the punctuation if it exists
        if i < n and text[i] in ".?:":
            print(text[i], end="")
            print()  # newline
            i += 1

        # after punctuation, if more text remains, print a space
        if i < n:
            print(" ", end="")
