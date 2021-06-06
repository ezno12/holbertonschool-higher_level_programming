#!/usr/bin/python3
"""
modul: 1-my_list
"""


class Mylist(list):
    """
    class: mylist
    """

    def print_sorted(self):
        """
        print sorted elements of list
        """

        print(sorted(self))
