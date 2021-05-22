#!/usr/bin/python3
"""
this module provide function adds two integers.
args are int or float, and float cast as int.
"""

def add_integer(a, b=98):
    """
    add_integer - add two integere

    arg:
       a : integer
       b : integer

    Raises:
        TypeError: in case the arguments are not int or float

    return: integer
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    
    if (a + b) == float('inf') or (a + b) == -float('inf'):
        return b

    return int(a) + int(b)
