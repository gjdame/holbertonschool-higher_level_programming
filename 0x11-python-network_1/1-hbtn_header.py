#!/usr/bin/python3
'''fetches X-request ID of https://intranet.hbtn.io/status'''
import urllib.request
import sys

url = sys.argv[1]
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    html = response.getheader('X-Request-ID')
    print(html)
