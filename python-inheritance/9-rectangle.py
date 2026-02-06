#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""

Rectangle = __import__('8-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a Square.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self._Rectangle__width * self._Rectangle__height

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)

    def __repr__(self):
        """Return the official string representation of the square."""
        return "Square({})".format(self._Rectangle__width)
