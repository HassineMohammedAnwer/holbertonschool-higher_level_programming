#!/bin/bash
#sends a JSON POST
curl -sX POST -H "Content-Type: application/json" -d $(cat "$2") "$1"
