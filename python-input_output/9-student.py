#!/usr/bin/python3
"z"

class Student:
    """
    Student class with public attributes and JSON dictionary representation.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieve a dictionary representation of the Student instance.

        Returns:
            dict: Dictionary containing all attributes of the instance.
        """
        return self.__dict__.copy()
