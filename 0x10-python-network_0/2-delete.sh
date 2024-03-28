#!/bin/bash
# takes in a URL, sends a request to that URL,
# and displays the size of the body of the response

if [ $# -ne 1 ];
then
	echo "Usage: $0 <URL>"
	exit 1
else
	curl -sX DELETE "$1"
fi
