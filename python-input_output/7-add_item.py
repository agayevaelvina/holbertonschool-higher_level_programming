#!/usr/bin/python3
"""
Script that adds all arguments to a Python list,
then saves them to a file using JSON format.

Usage: ./7-add_item.py <item1> <item2> ...
"""

import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

if __name__ == "__main__":
    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)
