#!/usr/bin/python3
"""
Write a function that converts a Roman numeral to an integer.
"""


def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
