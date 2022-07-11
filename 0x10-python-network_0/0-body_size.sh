#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response.
curl -w '%{size_download}\n' --silent --output /dev/null "$1"
