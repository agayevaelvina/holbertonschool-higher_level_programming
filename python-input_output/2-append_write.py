#!/usr/bin/python3
"""Appends a string to a UTF-8 text file and returns the number of characters added."""

def append_write(filename="", text=""):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
