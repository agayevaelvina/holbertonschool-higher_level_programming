#!/usr/bin/python3
"x"

class Student:
    """
    Student class with public attributes and JSON dictionary representation
    that can optionally filter attributes.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.

        If attrs is a list of strings, only those attributes are included.
        Otherwise, all attributes are included.

        Args:
            attrs (list, optional): List of attribute names to retrieve.

        Returns:
            dict: Dictionary representation of the instance.
        """
        if isinstance(attrs, list) and all(type(a) == str for a in attrs):
            # Filtered attributes only if they exist in the instance
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        else:
            # Return all attributes
            return self.__dict__.copy()
