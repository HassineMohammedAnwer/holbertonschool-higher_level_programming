#!/usr/bin/python3
"""5e52e160-c822-4669-8b3a-8b3bbca7b090
    -
    -"""
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
