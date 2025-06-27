#!/usr/bin/python3
"""
This module defines the Rectangle class with private width and height
attributes, including property getters and setters with type and value
validation, and methods to compute area and perimeter.
"""


class Rectangle:
    """Rectangle class with width and height properties, validation,
    and area and perimeter calculation methods."""

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
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle.
        If either width or height is 0, perimeter is 0."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
