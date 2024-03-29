#!/usr/bin/python3
"""Takes in an url  and displays the value of X-Request-Id header"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)

    print(res.headers.get('X-Request-Id'))
