#!/usr/bin/python3
"""Print text with a new line after each '.', '?', and ':' character."""


def text_indentation(text):
    """Print text with a new line after each '.', '?', and ':' character."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    n = len(text)

    while i < n:
        # Skip leading spaces
        while i < n and text[i] == " ":
            i += 1
        if i >= n:
            break

        # Print characters until punctuation
        while i < n and text[i] not in ".?:":
            print(text[i], end="")
            i += 1

        # Print the punctuation itself
        if i < n and text[i] in ".?:":
            print(text[i], end="")
            print()  # only one newline
            i += 1
