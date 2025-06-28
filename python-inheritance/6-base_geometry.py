#!/usr/bin/python3
"""Module that defines the BaseGeometry class with an unimplemented area method."""


class BaseGeometry:
    """Base class for geometry operations."""

    def area(self):
        """Raise an exception indicating the method is not implemented."""
        raise Exception("area() is not implemented")
