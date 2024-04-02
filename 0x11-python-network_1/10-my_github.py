#!/usr/bin/python3
"""
Takes in a Github username and password
Sends a post request with parameters
displays the id of the user from json response
"""
import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]

    auth = (username, password)
    res = requests.post(url, auth=auth)

    data = res.json()
    if data:
        myId = data.get('id')
        print(myId)
    else:
        print("None")
