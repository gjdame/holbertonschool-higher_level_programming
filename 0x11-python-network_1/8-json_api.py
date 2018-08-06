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
    data = r.json()

    try:
        id = data.get('id')

        name = data.get('name')
        if id == None or name == None:
            print("No result")
        else:
            print ("[{}] {}".format(id, name))
    except:
        print("Not a valid JSON")
