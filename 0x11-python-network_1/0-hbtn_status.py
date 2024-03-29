#!/usr/bin/python3
"""Fetches a url using urllib and prints the response"""
from urllib.request import Request, urlopen

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    req = Request(url)

    with urlopen(req) as response:
        res = response.read()

    print("Body response:")
    print("\t- type:", type(res))
    print("\t- content:", res)
    print("\t- utf8 content:", res.decode('utf-8'))
