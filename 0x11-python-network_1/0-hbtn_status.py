#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
   print("Body response:")
   html = response.read()
   print("\t- type:", type(html))
   print("\t- content:", html)
   print("\t- utf8 content:", html.decode('utf-8'))
