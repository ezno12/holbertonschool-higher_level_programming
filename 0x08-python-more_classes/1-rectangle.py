#!/usr/bin/python3
"""
Rectangle Modul
"""


class Rectangle:
    """
    Rectangle Class

     Attribute:
            width (int): Private
            height (int) : Private
    """
    def __init__(self, width=0, height=0):
        """
        initzaltion

        Args:
            width (int): The width of rectangle
            height (int): Thhe height of rectangle

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width
        Args:
            Value (int) : a value to set
        Raises:
            TypeError: When value is not int
            ValueError: When value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property   
    def height(self):
        """
        Getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height
        Args:
            Value (int) : a value to set
        Raises:
            TypeError: When value is not int
            ValueError: When value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
