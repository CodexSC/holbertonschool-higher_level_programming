#!/usr/bin/python3
"""Define a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of a Student instance."""
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance from a dictionary.

        Args:
            json (dict): The dictionary to reload attributes from.
        """
        for key, value in json.items():
            setattr(self, key, value)

    def __str__(self):
        """Return the print representation of a Student instance."""
        return f"[Student] {self.first_name} {self.last_name}"
