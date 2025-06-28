#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF-8) and returns
    the number of characters added.

    If the file doesn’t exist, it is created.

    Args:
        filename (str): The path to the file to append to.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
