#!/usr/bin/python3
"""Module that defines a function to check if object inherits from a specified class."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class; otherwise False."""
    return isinstance(obj, a_class) and type(obj) is not a_class
