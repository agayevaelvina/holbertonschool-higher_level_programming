#!/usr/bin/python3
"""
Module: lookup_module
This module provides a function to list the available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of the given object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list containing the names of the object's attributes and methods.
    """
    return dir(obj)
