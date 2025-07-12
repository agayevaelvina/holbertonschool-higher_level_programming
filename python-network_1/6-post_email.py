#!/usr/bin/python3
"""Sends a POST request"""

import requests
import sys

if __name__ == "__main__":
    """Ensure code is executed when directly run"""
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    response = requests.post(url, data=data)
    print(response.text)
