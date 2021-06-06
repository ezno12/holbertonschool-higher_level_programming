#!/usr/bin/python3
"""
    module: 7-base_geometry
"""


class BaseGeometry():
    """
    BaseGeometry class
    """

    def area(self):
        """
        public instance
        raise:
             Expection : area not used

        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        check if value is integer and sup then 0
        Args:
                name (string): name
                value(int): Value
            Raises:
                TypeError: When Value is not int
                ValueError: When Value less or equal to 0
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be greater than 0".format(name))
