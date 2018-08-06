#!/usr/bin/python3
'''fetches X-request ID of https://intranet.hbtn.io/status'''
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        html = response.getheader('X-Request-ID')
        print(html)
