#!/bin/bash
#sends a JSON POST
curl -X POST "$1" -H 'Content-Type: application/json' -d '$(cat "$2")'
