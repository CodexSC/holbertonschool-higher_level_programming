#!/usr/bin/python3
"""Module contains inherits_from function"""


def inherits_from(obj, a_class):
    """Return True if object is instance of a class that inherited from specified class"""
    return issubclass(type(obj), a_class)
