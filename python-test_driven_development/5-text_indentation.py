#!/usr/bin/python3
"""Module for text indentation."""


def text_indentation(text):
    """Print text with a newline after each '.', '?', and ':' character."""
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    n = len(text)
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if text == "":
        return
    buf = ""
    while i < n:
        c = text[i]
        buf += c
        if c in ".?:":
            print(buf.strip())
            buf = ""
            i += 1
            # Skip all spaces after punctuation
            while i < n and text[i] == ' ':
                i += 1
            continue
        i += 1
    if buf.strip():
        print(buf.strip())
