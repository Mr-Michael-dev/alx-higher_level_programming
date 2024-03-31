#!/usr/bin/python3
"""
Takes in a letter  and sends a post request with letter as parameter
displays the body of the response if json
"""
import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    res = requests.post(url, data={'q': q})

    if 'application/json' in res.headers.get('content-type'):
        data = res.json()

        if data:
            myId = data.get('id')
            name = data.get('name')
            print("[{}] {}".format(myId, name))
        else:
            print("No result")
    else:
        print("Not a valid JSON")
