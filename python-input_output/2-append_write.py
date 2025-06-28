#!/usr/bin/python3
"""
This module contains a function to append text to a UTF-8 file and returns the number of characters added.
"""
def append_write(filename="", text=""):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
