#!/usr/bin/python3
'''displays body of response after sending POST request with email'''
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            print(html)
    except urllib.error.HTTPError as e:
        code = e.code
        print("Error code: {:d}".format(code))
