#!/usr/bin/python3
"""
Prints text with two newlines after each '.', '?', or ':'
"""


def text_indentation(text):
    """Prints text with a newline after '.', '?', or ':', no extra newlines at the end."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            # Only print an extra newline if there are more characters after this
            if i != len(text) - 1:
                print("\n")
        i += 1
