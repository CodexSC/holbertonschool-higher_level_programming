#!/usr/bin/python3
"""Class to JSON function."""
import json


def class_to_json(obj):
    """Class to JSON function."""
    return obj.__dict__
