#!/bin/bash
# takes in a URL as args and sends a GET request to the URL
#then displays the body of the response
curl -sL "$1"
