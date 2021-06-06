#!/usr/bin/python3
"""
    modul: 8-rectangle.py
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class
    """
    def __init__(self, width, height):
        """
        intialize
        """
        self.ininteger_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
