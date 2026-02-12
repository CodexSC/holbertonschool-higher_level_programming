#!/usr/bin/python3
"""Writes a string to a text file (UTF8) and returns
the number of characters written
"""


def write_file(filename="", text=""):
    """Write text to a UTF-8 file and return the character count."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
