#!/bin/bash
#sends a JSON POST
curl -s POST -H "Content-Type: application/json" -d $(cat "$2") "$1"
