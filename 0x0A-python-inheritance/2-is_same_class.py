#!/usr/bin/python3
"""
modul: 2-is_same_class
"""


def is_same_class(obj, a_class):
    """
    return true if object == an instance of specified class or other wise false
    """

    return isinstance(a_class, type(obj))
