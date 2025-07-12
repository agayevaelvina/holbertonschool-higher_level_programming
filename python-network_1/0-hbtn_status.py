#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""

from urllib import request

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    req = request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

    with request.urlopen(req) as response:
        body = response.read()
        utf8_content = body.decode('utf-8')

    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", utf8_content)
