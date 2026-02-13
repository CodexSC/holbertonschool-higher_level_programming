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

    @classmethod
    def update(cls, instance, key, value):
        """Update the attribute of a student instance.
        Args:
            instance (Student): The student instance to update.
            key (str): The key of the attribute to update.
            value (str): The new value of the attribute.
        """
        if key in instance.__dict__:
            instance.__dict__[key] = value
