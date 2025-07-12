#!/usr/bin/python3
"""Sends a request and handles HTTP errors"""

import sys
from urllib import request, error

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            body = response.read().decode("utf-8")
            print(body)
    except error.HTTPError as e:
        print("Error code:", e.code)
