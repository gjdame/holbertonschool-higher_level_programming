#!/usr/bin/python3
'''fetches status of https://intranet.hbtn.io/status'''
import requests
import sys

if __name__ == "__main__":

    data = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=data)
    print(r.text)
