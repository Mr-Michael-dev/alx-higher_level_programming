#!/bin/bash
# takes in a URL, sends a request to that URL,and displays all HTTP methods the server will accept
curl -sI "$1" | grep -i Allow | cut -d " " -f 2-
