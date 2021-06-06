#!/usr/bin/python3
"""
modul: 10-square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square:
    """
    Class sqaure
    """
    def __init__(self, size):
        """
        Initialize
        """
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """
        calc square
        """
        return self.__size ** 2

    def __str__(self):
        """
            __str__
        """
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
