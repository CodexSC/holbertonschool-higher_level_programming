#!/usr/bin/python3
"""Module that contains inherits_from function"""


def inherits_from(obj, a_class):
    """Check if obj is instance of a class that inherited from a_class"""
    try:
        return issubclass(type(obj), a_class)
    except TypeError:
        return False
