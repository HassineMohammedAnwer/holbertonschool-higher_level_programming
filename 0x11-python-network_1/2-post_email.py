#!/usr/bin/python3
"""urllib.request.urlopen(sys.argv[1]) as response"""
from urllib import request, parse
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    email = argv[2]
    data = parse.urlencode({'email': email})
    data = data.encode("ascii")
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))

