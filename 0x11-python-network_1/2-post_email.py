#!/usr/bin/python3
"""
Sends a request to the URL and displays
the value of the X-Request-Id variable found in the header
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

    print('Your email is: ', res.decode('utf-8'))
