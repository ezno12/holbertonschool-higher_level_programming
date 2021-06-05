#!/usr/bin/python3
"""
modul: 6-load_from_json_file
"""
import json


def load_from_json_file(filename):
    """
    creat object from JSON file
    """
    with open(filename, "w", encoding='utf-8') as f:
        return json.load(f)