#!/usr/bin/python3
"""
Write a function that converts a Roman numeral to an integer.
"""


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
