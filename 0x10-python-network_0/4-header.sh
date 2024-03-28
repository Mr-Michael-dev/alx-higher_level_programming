#!/bin/bash
# takes in a URL, sends a GET request to that URL, and displays the body of the response
curl -sX GET -H "X-School-User-Id=98" "$1"
