#!/usr/bin/python3
#!/usr/bin/python3
"""
Script that adds all arguments to a Python list,
then saves them to a file using JSON format.
"""

import sys
import json

def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    """Creates an object from a JSON file."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

filename = "add_item.json"

if __name__ == "__main__":
    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)
