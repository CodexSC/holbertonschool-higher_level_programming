#!/usr/bin/python3
"""Module for text indentation."""


def text_indentation(text):
    """Print text with a newline after each '.', '?', and ':' character, skipping spaces after punctuation."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if text == "":
        return
    i = 0
    n = len(text)
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
