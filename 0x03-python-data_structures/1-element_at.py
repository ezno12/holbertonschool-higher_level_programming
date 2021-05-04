#!/usr/bin/python3

"""
 * element_at - function that retrieves an element from a list.
 *
 * @my_list: integer list.
 * @idx: the index of element.

"""
def element_at(my_list, idx):
    if idx < 0:
        return None
    if idx > len(my_list):
        return None
    else:
        my_list.count(idx)
