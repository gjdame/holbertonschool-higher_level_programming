#!/usr/bin/python3
'''fetches status of https://intranet.hbtn.io/status'''
import requests
import sys

if __name__ == "__main__":

    try:
        rep = sys.argv[1]
    except:
        rep = ""

    data = {'q': rep}

    r = requests.post('http://0.0.0.0:5000/search_user', data=data)

    try:
        data = r.json()
        id = data.get('id')

        name = data.get('name')
        if id is None or name is None:
            print("No result")
        else:
            print("[{}] {}".format(id, name))
    except:
        print("Not a valid JSON")
