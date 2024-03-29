#!/usr/bin/python3
"""
Sends a request to the URL and displays
the value of the X-Request-Id variable found in the header
"""
from urllib.request import Request, urlopen
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = Request(url)

    with urlopen(req) as response:
        res = response.getheader("X-Request-Id")

    print(res)
