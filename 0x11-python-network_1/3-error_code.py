#!/usr/bin/python3
"""urllib.request.urlopen(sys.argv[1]) as response"""
from urllib import request
from urllib.error import HTTPError
from sys import argv


if __name__ == '__main__':

    """mjk mk jm qaae dok"""
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
            print("Error code: {}".format(e.code))
