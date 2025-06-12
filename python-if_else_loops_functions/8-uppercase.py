#!/usr/bin/python3
def uppercase(str):
    print("".join(
        "{}".format(chr(ord(c) - 32)) if 'a' <= c <= 'z' else "{}".format(c)
        for c in str
    ))
