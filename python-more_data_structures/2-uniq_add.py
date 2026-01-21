#!/usr/bin/python3
"""
Write a function that adds all unique integers
in a list (only once for each integer).
"""


def uniq_add(my_list=[]):
    result = 0
    for i in set(my_list):
        result += i
    return result
