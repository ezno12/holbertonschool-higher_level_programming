#!/usr/bin/python3
"""
this module provide function print new lines after . and ?
args is string.
"""

def text_indentation(text):
    """
    text_indentation - print new lines after . and ?

    :param text: string

    raise:
        TypeError: if text not string

    :return: text
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    a = 0
    while a < len(text):
        if text[a] in [':', '.', '?']:
            print(text[a])
            print()
            a += 1
        else:
            print(text[a], end='')
        a += 1
