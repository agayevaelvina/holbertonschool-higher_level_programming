#!/usr/bin/python3
"""
This module defines the Rectangle class with private width and height,
property getters/setters with validation, public class attribute
number_of_instances, area and perimeter methods, printable string with '#',
eval-able repr, and a deletion message.
"""


class Rectangle:
    """Rectangle class with width and height properties, validation,
    a class attribute to count instances, area and perimeter methods,
    printable string, eval-able repr, and a deletion message."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize rectangle and increment instance counter."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """Return the rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Return the rectangle perimeter or 0 if width or height is 0."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Printable string using '#' characters."""
        if self.width == 0 or self.height == 0:
            return ""
        lines = ['#' * self.width for _ in range(self.height)]
        return "\n".join(lines)

    def __repr__(self):
        """Return string to recreate the instance via eval()."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message when an instance is deleted and decrement counter."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
