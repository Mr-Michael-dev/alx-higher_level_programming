#!/bin/bash
# takes in a URL, sends a GET request to that URL, and displays the size of the body of a 200 status code response
curl -sLX GET "$1"

