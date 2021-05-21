#!/usr/bin/python3
"""
this module pprint two argement most be string.
args are two string.
"""

def say_my_name(first_name, last_name=""):
    """
    say_m_name - print the first name and last name

    :param first_name: string
    :param last_name: strin

    raise:
         TypeError: in case args not strings

    :return:
    """

    if first_name is None or not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
