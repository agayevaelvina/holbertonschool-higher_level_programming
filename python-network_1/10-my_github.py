#!/usr/bin/python3
"""Takes GitHub credentials and displays id"""
import requests
import sys

if __name__ == "__main__":
    """Ensure code is executed when directly run"""
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        user_data = response.json()
        print(user_data.get("id"))
    else:
        print("None")
