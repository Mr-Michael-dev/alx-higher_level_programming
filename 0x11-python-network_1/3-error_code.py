#!/usr/bin/python3
"""
Sends a request to the URL and displays the value of the response
"""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = Request(url)

    try:
        with urlopen(req) as response:
            res = response.read()
    except HTTPError as e:
        print('Error code:', e.code)
    else:
        print(res.decode('utf-8'))
