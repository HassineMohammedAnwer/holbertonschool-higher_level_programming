#!/usr/bin/python3
"""
urllib.request.urlopen(sys.argv[1]) as response"""
if __name__ == '__main__':
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        res = response.headers.get('X-Request-Id')
        print(res)

