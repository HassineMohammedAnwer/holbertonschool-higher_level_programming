#!/bin/bash
#takes in a URL as an argument, sends a GET
curl -sX GET -H "X-HolbertonSchool-User-Id: 98" "$1"
