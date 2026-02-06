#!/usr/bin/python3
"""Defines a Square class."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, inherits from Rectangle."""

    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size (int): Size of the square
        """
        self.integer_validator("size", size)

        self.__size = size

        super().__init__(size, size)
