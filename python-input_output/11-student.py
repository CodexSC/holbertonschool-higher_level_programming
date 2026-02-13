#!/usr/bin/python3
""" Student class """


class Student:
    """ Student class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)

        return self

    def __str__(self):
        return f"[Student] {self.first_name} {self.last_name}"

        return self
