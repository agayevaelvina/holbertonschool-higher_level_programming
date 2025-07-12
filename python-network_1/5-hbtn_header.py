#!/usr/bin/python3
""" Sends a request and displays the value in the header"""
import requests
import sys

if __name__ == "__main__":
    """Ensure code is executed when directly run"""
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))
