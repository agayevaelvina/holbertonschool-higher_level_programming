#!/usr/bin/python3
"""This module provides utility functions for working with files and JSON serialization."""


def to_json_string(my_obj):
    """
    Returns the JSON representation of my_obj (as a string).

    Args:
        my_obj (any): The object to serialize to JSON.

    Returns:
        str: JSON string representation of my_obj.
    """
    import json
    return json.dumps(my_obj)
