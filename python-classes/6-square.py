#!/usr/bin/python3
"""
Defines a square by: (based on 0-square.py)
Private instance attribute: size
"""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """
        Initialize a new square.

        Args:
            size (int): The size of the new square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        # Store size as a private attribute (name mangling with __)
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

 @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using #."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            for _ in range(self.__size):
                print("#", end="")
            print()

