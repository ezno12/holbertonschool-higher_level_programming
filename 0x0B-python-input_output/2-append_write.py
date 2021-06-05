#!/usr/bin/python3
"""
Modul: 2-append_write
"""

def append_write(filename="", text=""):
    """
    append a string to the end of a text file
    """

    with open(filename, "a", encoding="uft-8") as file:
        file.write(text)
    return len(text)
