#!/usr/bin/python3
"""Module that contains a function that prints a name."""


def say_my_name(first_name, last_name=""):
    """Prints a name."""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    name = "My name is {}".format(first_name)
    if last_name:
        name += " {}".format(last_name)
    print(name)
