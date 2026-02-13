#!/usr/bin/python3
"""Class to JSON function."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure for JSON serialization of an object."""
    return {key: value for key, value in obj.__dict__.items() if isinstance(value, (list, dict, str, int, bool))}
