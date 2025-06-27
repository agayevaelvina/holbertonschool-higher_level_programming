#!/usr/bin/python3
"""
This module defines the Rectangle class with private width and height
attributes, property getters/setters with validation, area and perimeter
methods, string representation using '#' characters, and a repr method
for recreating the instance.
"""


class Rectangle:
    """Rectangle class with width and height properties, validation,
    area and perimeter methods, printable string, and eval-able repr."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
