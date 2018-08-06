#!/usr/bin/python3
'''fetches status of https://intranet.hbtn.io/status'''
import requests
import sys

if __name__ == "__main__":

    user = sys.argv[1]
    pwd = sys.argv[2]
    r = requests.get("https://api.github.com/user",
                     auth=(sys.argv[1], sys.argv[2]))
    data = r.json()
    id = data.get('id')
    print(id)
