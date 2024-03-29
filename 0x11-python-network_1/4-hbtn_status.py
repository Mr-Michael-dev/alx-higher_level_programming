#!/usr/bin/python3
"""Fetches a url using requests module and prints the response"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    req = requests.get(url)

    print("Body response:")
    print("\t- type:", type(req.text))
    print("\t- content:", req.text)
