#!/usr/bin/python3
"""Module that defines a function to check if object is an instance or inherits from a class."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance or inherits from a_class, otherwise False."""
    return isinstance(obj, a_class)
