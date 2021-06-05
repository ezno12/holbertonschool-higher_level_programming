#!/usr/bin/python3
"""
Module: 0-read-file
"""

def read_file(filename=""):
    """
    Read_file - function to read a text file and lrint stdout
    """
    if filename is None:
        return None

    with open(filename, encoding="utf-8", mode="r") as file:
        text = file.read()

    print(text, end="")
