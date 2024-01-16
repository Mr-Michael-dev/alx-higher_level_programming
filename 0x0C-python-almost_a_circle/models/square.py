#!/usr/bin/python3
"""
This module represents Square Class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inheriting from Rectangle class

    Methods:
        __init__(): instantiation method for square
        __str__(): returns string representation of square attributes
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        initializes the square using the logic of the __init__ of the Rectangle

        Args:
            size: size of the Square
            x (int): x-cordinate
            y (int): y-cordinate
            id: id of the Square
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        returns the string representation of Square
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
