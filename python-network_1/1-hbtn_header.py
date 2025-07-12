#!/usr/bin/python3
import sys
from urllib import request

url = sys.argv[1]

with request.urlopen(url) as response:
    headers = response.info()
    print(headers.get('X-Request-Id'))
