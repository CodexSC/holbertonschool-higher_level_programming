#!/usr/bin/python3
"""Defines a Rectangle class."""

class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise ValueError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
