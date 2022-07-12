#!/usr/bin/python3
"""Body response:$
    - type: <class 'str'>$
    - content: OK$"""
import requests


if __name__ == '__main__':
    url = 'https://intranet.hbtn.io/status'
    response = requests.get(url)
    print("Body response:")
    print("\t- type:", type(response))
    print("\t- content:", response)
