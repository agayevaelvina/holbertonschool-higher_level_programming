#!/usr/bin/python3
"x"

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using its JSON representation.

    Args:
        my_obj (any): The object to serialize and write.
        filename (str): The name of the file to write to.
    """
    import json
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
