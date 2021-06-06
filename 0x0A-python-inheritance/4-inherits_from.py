#!/usr/bin/python3
"""
Modul: 4-inherits_from
"""


def inherits_from(obj, a_class):
    """
    return ture if instance inheret directly or indirectly from class
    other wise return false
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
