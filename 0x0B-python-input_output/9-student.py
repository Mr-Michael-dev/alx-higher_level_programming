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

        if not isinstance(age, int) or age <= 0:
            raise TypeError("age must be an integer and greater than 0")
        else:
            self.age = age

        self.first_name = first_name
        self.last_name = last_name

    def to_json(self):
        """
        Retrieves a dictionary representation of a student instance
        """
        my_dict = {}

        attributes = self.__dict__

        for attr_name, attr_value in attributes.items():
            if isinstance(attr_value, (dict, list, int, str, bool)):
                my_dict[attr_name] = attr_value

        return my_dict
