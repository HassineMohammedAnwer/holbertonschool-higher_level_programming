#!/usr/bin/python3
"""urllib.request.urlopen(sys.argv[1]) as response"""
import requests


if __name__ == '__main__':
    url = 'https://intranet.hbtn.io/status'
    content = requests.get(url).text
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
