#!/usr/bin/python3
"""
Modul: 2-append_write
"""


def append_write(filename="", text=""):
    """
    append a string to the end of a text file
    """
    with open(filename, "a", encoding="uft-8") as f:
        f.write(text)
    return len(text)
