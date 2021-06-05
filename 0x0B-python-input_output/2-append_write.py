#!/usr/bin/python3
"""
Modul: 2-append_write
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)

