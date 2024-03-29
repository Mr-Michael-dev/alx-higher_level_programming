#!/usr/bin/python3
"""
Sends a post request to the URL with email data and displays response body
"""
from urllib.request import Request, urlopen
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    data = "email=" + sys.argv[2]
    data = data.encode('ascii')
    req = Request(url, data)

    with urlopen(req) as response:
        res = response.read()

    print(res.decode('utf-8'))
