#!/usr/bin/python3

"""
 * print_list_integer - function all integers of a list.
 *
 * @my_list: list of integer.

"""

def print_list_integer(my_list=[]):
    for x in range(0, len(my_list)):
        print("{:d}".format(my_list[x]))
