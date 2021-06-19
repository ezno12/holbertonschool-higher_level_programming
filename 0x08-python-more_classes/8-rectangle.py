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
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        initzaltion

        Args:
            width (int): The width of rectangle
            height (int): Thhe height of rectangle

        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            raise ValueError("width must be >= 0")
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
            raise ValueError("height must be >= 0")
        self.__height = value
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        return bigger rectangle
        """
        area1 = rect_1.width * rect_1.height
        area2 = rect_2.width * rect_2.height

        
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (area1 >= area2):
            return rect_1
        return rect_2

    def area(self):
        """
        calcul area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        calcul perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return(self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        print rectangle with characeter #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        string = ""
        for i in range(self.__height):
            string += (str(self.print_symbol) * (self.__width) + "\n")
        return string[0:-1]

    def __repr__(self):
        """
        string representation of the rectangle
        """
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """
        print a msg when instance deleted
        """
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
