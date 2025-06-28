#!/usr/bin/python3
"x"

def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer, boolean) for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: Dictionary of the object's attributes.
    """
    return obj.__dict__.copy()
