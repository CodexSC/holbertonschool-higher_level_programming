#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """
    Function to find and return the max integer (or float) in a list of numbers.

    Args:
        list (list): A list of numbers (ints or floats).

    Returns:
        The maximum number in the list.
        Returns None if the list is empty.

    Raises:
        TypeError: If list is not a list.
    """
    if not isinstance(list, list):
        raise TypeError("list must be of type list")
    if len(list) == 0:
        return None
    result = list[0]
    for i in list[1:]:
        if i > result:
            result = i
    return result
