#!/usr/bin/python3
"""
This module contains the BaseGeometry class with basic validation methods.
"""

class BaseGeometry:
    """
    Base class for geometry objects.
    Provides a method to validate integer values.
    """
    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.

        Args:
            name (str): The name of the value (used in exception messages).
