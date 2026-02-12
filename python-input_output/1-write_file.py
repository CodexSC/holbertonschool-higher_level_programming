#!/usr/bin/python3
"""Writes a string to a text file (UTF8) and returns
the number of characters written
"""
with open("my_file_1.txt", "w", encoding="utf-8") as f:
    return f.write(text)
