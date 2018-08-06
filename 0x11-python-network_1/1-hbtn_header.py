#!/usr/bin/python3
'''fetches status of https://intranet.hbtn.io/status'''
import urllib.request
import sys

url = sys.argv[1]
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    html = response.info()
    print(html.get('X-Request-Id'))
