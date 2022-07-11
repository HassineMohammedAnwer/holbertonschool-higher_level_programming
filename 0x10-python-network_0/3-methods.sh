#!/bin/bash
# Displays HTTP methods the server will accept
curl -v -X OPTIONS "$1" | grep "Allow: " | cut -d' ' -f 2-
