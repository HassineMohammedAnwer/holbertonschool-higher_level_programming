#!/usr/bin/python3
import urllib.request as request
from sys import argv


if __name__ == '__main__':
    with request.urlopen(argv[1]) as response:
        head = response.headers.get('X-Request-Id')
        print(head)

