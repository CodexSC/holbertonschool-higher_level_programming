#!/usr/bin/python3


"""
Defines a square by: (based on 0-square.py)
Private instance attribute: size
"""


class Square:
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.


        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        #Validate that size is an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

    #Stores size as a private attribute (name mangling with __)
        self.__size = size
