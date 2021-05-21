#!/usr/bin/python3
"""
this module provide function print (#) square of integers.
args is int
"""

def print_square(size):
    """
    print_square - print (#) square of integers.

    :param size: int

    raise:
         TypeError: if size not integer or float less then zero
         ValueError: size less then zero

    :return: printed square (#)
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end ="")
        print()
