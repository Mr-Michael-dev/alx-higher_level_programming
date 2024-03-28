#!/bin/bash
# takes in a URL, sends a GET request to that URL,
# and displays the size of the body of a 200 status code response

if [ $# -ne 1 ];
then
	echo "Usage: $0 <URL>"
	exit 1
fi

#response_code=$(curl -sX GET "$1" -w "%{http_code]")

#if [ "$response_code" -ne 200 ];
#then
#	echo "Error: Server returned non-2-- status code: $response_code"
#	exit 1
#fi

response=$(curl -sX GET "$1")

echo "$response"
