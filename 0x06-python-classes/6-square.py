#!/usr/bin/python3
"""
Module for Square class
"""


class Square:
    """
    class Square: contains getter/setter properties for 'size'
    and functions to calculate area and print the square
    """
    def __init__(self, size):
        """
        initializes Square with 'size'
        """
        self.handle_errors(size)
        self.__size = size

    @property
    def size(self):
        """
        size getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size setter
        """
        self.handle_errors(value)
        self.__size = value

    def area(self):
        """
        calculates the area of a square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        prints square based on 'size'
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()

    def handle_errors(self, value):
        """
        checks if size is an integer and is >=0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """
        get attribute position
        """
        return self.__posistion

    @position.setter
    def position(self, value):
        """
        setter of position

        arg:
            value: tuple
        """

        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
