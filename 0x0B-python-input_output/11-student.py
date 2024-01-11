#!/usr/bin/python3
"""
This module represents a Student class
"""


class Student:
    """
    Student class

    Attr:
        first_name
        last_name
        age

    Methods:
        __init__ - instantiation method
        to_json - custom serialization method
    """

    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        """
        instantiation method

        args:
            first_name (str): first name of student
            last_name (str): last name of student
            age (int): age of student
        """

        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a student instance
        If attrs is a list of strings,
        only attribute names contained in this list must be retrieved.

        args:
            attrs: list of attributes

        Returns:
            A dictionary
        """
        my_dict = {}

        attributes = self.__dict__

        for attr_name, attr_value in attributes.items():
            if isinstance(attr_value, (dict, list, int, str, bool)):
                if isinstance(attrs, list):
                    for name in attrs:
                        if name == attr_name:
                            my_dict[attr_name] = attr_value
                else:
                    my_dict[attr_name] = attr_value

        return my_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance based on a JSON dictionary

        Args:
            json: dictionary representing attribute names and values
        """
        for key, value in json.items():
            setattr(self, key, value)
