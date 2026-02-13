#!/usr/bin/python3
"""Function that returns an object (Python data structure) represented
by a json string"""


import json


def from_json_string(my_str):
    """Function that returns an object (Python data structure) represented
    by a json string"""
    return json.loads(my_str)
