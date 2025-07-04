#!/usr/bin/env python3
import json
import os

def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.

    Parameters:
    - data (dict): The data to serialize.
    - filename (str): The name of the file to write the JSON data to.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_and_deserialize(filename):
    """
    Loads JSON data from a file and deserializes it into a Python dictionary.

    Parameters:
    - filename (str): The name of the file to read the JSON data from.

    Returns:
    - dict: The deserialized data.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
