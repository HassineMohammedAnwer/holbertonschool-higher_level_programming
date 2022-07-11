#!/bin/bash
# takes in a URL as args and sends a GET request to the URL
curl -sX GET "$1" -L 200
