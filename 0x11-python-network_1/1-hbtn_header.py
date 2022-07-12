#!/usr/bin/python3
"""fetches the url as arg"""
import urllib.request as req
from sys import argv

if __name__ == '__main__':
    with req.urlopen(argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
