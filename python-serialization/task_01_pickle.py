#!/usr/bin/python3
"""Module for saving and loading objects using JSON files."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation.

    Args:
        my_obj: The object to save.
        filename (str): The name of the file to write to.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """Create an object from a JSON file.

    Args:
        filename (str): The name of the file to read from.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    my_list = [1, 2, 3]
    save_to_json_file(my_list, "my_list.json")
    print(load_from_json_file("my_list.json"))
    my_dict = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    save_to_json_file(my_dict, "my_dict.json")
    print(load_from_json_file("my_dict.json"))
