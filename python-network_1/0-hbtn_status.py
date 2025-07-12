#!/usr/bin/python3
"""Fetches a URL and displays response details"""

from urllib import request

if __name__ == "__main__":
    url = "http://0.0.0.0:5050/status"

    with request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode("utf-8"))
