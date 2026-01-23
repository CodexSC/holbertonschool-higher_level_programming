#!/usr/bin/python3
"""
Prints text with two newlines after each '.', '?', or ':'
"""


def text_indentation(text):
    """
    Prints text with two newlines after each '.', '?', or ':',
    except after the last character of the string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            # Check if not at the end to add extra newline
            if i != len(text) - 1:
                print("\n")
        i += 1
