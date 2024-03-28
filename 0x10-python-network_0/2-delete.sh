#!/bin/bash
# takes in a URL, sends a DELETE request to that URL, and displays the size of the body of the response
curl -sX DELETE "$1"
