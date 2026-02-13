#!/usr/bin/python3
"""Module for saving and loading objects using pickle serialization."""
import pickle


def save_to_json_file(my_obj, filename):
    """Serialize and save an object to a file using pickle.

    Args:
        my_obj: The object to save.
        filename (str): The name of the file to write to.
    """
    with open(filename, "wb") as f:
        pickle.dump(my_obj, f)


def load_from_json_file(filename):
    """Load and deserialize an object from a pickle file.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        The deserialized Python object.
    """
    with open(filename, "rb") as f:
        return pickle.load(f)
