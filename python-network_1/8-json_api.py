#!/usr/bin/python3
"""Takes in a letter and sends a POST request"""
import requests
import sys

if __name__ == "__main__":
    """Ensure code is executed when directly run"""
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}
    response = requests.post(url, data=data)
    try:
        json_data = response.json()
        if json_data:
            print(f"[{json_data.get('id')}] {json_data.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
