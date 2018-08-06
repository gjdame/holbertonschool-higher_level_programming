#!/usr/bin/python3
'''fetches status of https://intranet.hbtn.io/status'''
import requests
import sys

if __name__ == "__main__":

    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
