#!/bin/bash
# takes in a URL, sends a POST request to that URL, and displays the body of the response
curl -sX POST -d "email=test@email.com&subject=I+will+always+be+here+for+PLD" "$1"
