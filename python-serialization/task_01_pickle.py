#!/usr/bin/env python3
import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints the attributes of the object.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the object and saves it to a file using pickle.

        Parameters:
        - filename (str): The name of the file to save the serialized object.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception as e:
            print(f"Serialization failed: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an object from a file using pickle.

        Parameters:
        - filename (str): The name of the file to load the object from.

        Returns:
        - CustomObject or None if deserialization fails.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                else:
                    print("Deserialized object is not a CustomObject instance.")
                    return None
        except (FileNotFoundError, pickle.PickleError, EOFError, Exception) as e:
            print(f"Deserialization failed: {e}")
            return None
