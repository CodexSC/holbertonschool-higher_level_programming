#!/usr/bin/python3
"""Class to JSON function."""
import json


def class_to_json(obj):
    """Class to JSON function."""
    return obj.__dict__

if __name__ == "__main__":
    my_list = []
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    print(class_to_json(my_list))
