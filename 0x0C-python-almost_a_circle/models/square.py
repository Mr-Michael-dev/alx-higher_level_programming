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

    def update(self, *args, **kwargs):
        """
        Updates square attributes with arguments supplied.
        If args is present and not empty, skip kwargs

        Args:
            *args: variable number of arguments
                - If one argument is provided, assume it's the id.
                - If more than one argument is provided,
                update id, size, x, and y in order.
            **kwargs: a dictionary of keywords and value
            """

        if args and len(args) > 0:
            """update attributes base on args"""
            # Update id if at least one argument is provided
            self.id = args[0]

            if len(args) >= 2:
                # Update width and height if at least two arguments provided
                self.int_validator("size", args[1])
                self.size = args[1]

            if len(args) >= 3:
                # Update x if at least four arguments are provided
                self.x_and_y_validator("x", args[2])
                self.x = args[2]

            if len(args) >= 4:
                # Update y if at least five arguments are provided
                self.x_and_y_validator("y", args[3])
                self.y = args[3]
        elif kwargs:
            # Update attributes based on kwargs
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value  # Update id
                elif key == 'size':
                    self.int_validator("size", value)
                    self.size = value
                elif key == 'x':
                    self.x_and_y_validator("x", value)
                    self.x = value
                elif key == 'y':
                    self.x_and_y_validator("y", value)
                    self.y = value
        else:
            pass
