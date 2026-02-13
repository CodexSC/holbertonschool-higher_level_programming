
#!/usr/bin/python3
"""Module for serializing and deserializing custom objects using pickle."""
import pickle


class CustomObject:
    """Represent a custom object with name, age, and student status."""

    def __init__(self, name, age, is_student):
        """Initialize a new CustomObject.

        Args:
            name (str): The name of the object.
            age (int): The age of the object.
            is_student (bool): The student status of the object.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance and save it to a file.

        Args:
            filename (str): The name of the file to save to.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return an instance of CustomObject from a file.

        Args:
            filename (str): The name of the file to load from.

        Returns:
            CustomObject: The deserialized object, or None if an error occurs.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None

