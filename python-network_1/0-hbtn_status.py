#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""

from urllib import request

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    headers = {"User-Agent": "Mozilla/5.0"}

    req = request.Request(url, headers=headers)

    with request.urlopen(req) as response:
        body = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode("utf-8"))
