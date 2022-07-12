#!/usr/bin/python3
"""5e52e160-c822-4669-8b3a-8b3bbca7b090
    -
    -"""
import requests
import sys


if __name__ == '__main__':
    response = requests.get("https://api.github.com/user",
                            auth=(sys.argv[1], sys.argv[2]))
    jresponse = response.json()
    try:
        print(jresponse['id'])
    except KeyError:
        print('None')
