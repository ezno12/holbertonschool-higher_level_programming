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

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text):
        if text[c] in [".", "?", ":"]:
            print(text[c])
            print()
            c += 1
        else:
            print(text[c], end="")
            c += 1
