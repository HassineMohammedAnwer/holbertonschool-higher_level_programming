#!/usr/bin/python3
"""5e52e160-c822-4669-8b3a-8b3bbca7b090
    -
    -"""
import requests
import sys


if __name__ == '__main__':
    response = requests.get(sys.argv[1])
    if ((response.status_code >= 400) and (response.status_code <= 599)):
        print('Error code: {}'.format(response.status_code))
    else:
        print(response.text)
