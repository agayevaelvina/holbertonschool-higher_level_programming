#!/usr/bin/python3
"""
This module contains a function to append text to a UTF-8 file and returns the number of characters added.
"""
def append_write(filename="", text=""):
    """
    Appends a string at the end of a UTF-8 text file and returns the number of characters added.

    If the file does not exist, it will be created.

    Args:
        filename (str): The name of the file.
        text (str): The text string to append.

    Returns:
        int: The number of characters added to the file.
    """


    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
