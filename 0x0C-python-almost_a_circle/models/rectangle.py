#!/usr/bin/python3
"""
This module represents rectangle class which is a subclass of Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class inherits from base.

    Attributes:
        __width -> width
        __height -> height
        __x -> x
        __y -> y

    Methods:
        __init__(): instantiation method
        int_validator(name, value): Validates if the value is an integer > 0
        x_and_y_validator(name, value): Validates if the value is an int >= 0
        area(): computes the area of rectangle
        display(): prints in stdout the rectangle instance with character '#'
        __str__(): returns formatted string representation of rectangle
    """

    __width = 0
    __height = 0
    __x = 0
    __y = 0

    def int_validator(self, name, value):
        """
        Checks if the value inputted is an integer and > 0

        Args:
            name (str): name of the value to check
            value: value to be checked

        Raises:
            TypeError: if not an integer
            Value Error: if value <= 0
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    def x_and_y_validator(self, name, value):
        """
        Checks if the value inputted is an integer and >= 0

        Args:
            name (str): name of the value to check
            value: value to be checked

        Raises:
            TypeError: if not an integer
            Value Error: if value < 0
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiation method. Calls the super class with id.

        Args:
            width: width of the rectangle
            height: height of the rectangle
            x (int): x-cordinate
            y (int): y-cordinate
            id: id of the rectangle
        """

        super().__init__(id)
        self.int_validator("width", width)
        self.int_validator("height", height)
        self.x_and_y_validator("x", x)
        self.x_and_y_validator("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.int_validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.int_validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.x_and_y_validator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.x_and_y_validator("y", value)
        self.__y = value

    def area(self):
        """
        computes the area of Rectangle

        Returns:
            The product of width and height
        """
        return (self.width * self.height)

    def display(self):
        """
        prints to stdout the rectangle instance with character '#'
        """
        print_symbol = '#'

        for _ in range(self.y):
            print()

        for i in range(self.height):
            print(" " * self.x + print_symbol * self.width)  # Print single row

    def __str__(self):
        """Returns string representation of rectangle"""

        _str = f"[Rectangle] ({self.id}) {self.x}/{self.y}\
 - {self.width}/{self.height}"

        return _str

    def update(self, *args, **kwargs):
        """
        Updates rectangle attributes with arguments supplied.
        If args is present and not empty, skip kwargs

        Args:
            *args: variable number of arguments
                - If one argument is provided, assume it's the id.
                - If more than one argument is provided,
                update id, width, height, x, and y in order.
            *"kwargs: a dictionary of keywords and value
        """

        if args and len(args) > 0:
            """update attributes base on args"""

            # Update id if at least one argument is provided
            super().__init__(args[0])

            if len(args) >= 2:
                # Update width and height if at least two arguments provided
                self.int_validator("width", args[1])
                self.__width = args[1]

            if len(args) >= 3:
                # Update height if at least three arguments are provided
                self.int_validator("height", args[2])
                self.__height = args[2]

            if len(args) >= 4:
                # Update x if at least four arguments are provided
                self.x_and_y_validator("x", args[3])
                self.__x = args[3]

            if len(args) >= 5:
                # Update y if at least five arguments are provided
                self.x_and_y_validator("y", args[4])
                self.__y = args[4]
        elif kwargs:
            # Update attributes based on kwargs
            for key, value in kwargs.items():
                if key == 'id':
                    super().__init__(value)  # Update id
                elif key == 'width':
                    self.int_validator("width", value)
                    self.__width = value
                elif key == 'height':
                    self.int_validator("height", value)
                    self.__height = value
                elif key == 'x':
                    self.x_and_y_validator("x", value)
                    self.__x = value
                elif key == 'y':
                    self.x_and_y_validator("y", value)
                    self.__y = value
        else:
            pass

    def to_dictionary(self):
        """
        Reeturns the dictionary representation of Rectangle
        """

        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}
