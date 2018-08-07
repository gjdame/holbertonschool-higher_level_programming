#!/usr/bin/python3
'''fetches status of https://intranet.hbtn.io/status'''
import requests
import sys

if __name__ == "__main__":

    param = sys.argv[1]
    req = 'https://swapi.co/api/people/?search=' + param

    r = requests.get(req)

    data = r.json()
    count = data.get('count')

    print("Number of results: {}".format(count))

    while (1):
        results = data.get('results')
        for dic in results:
            name = dic.get('name')
            print(name)
        req = data.get('next')
        if req is None:
            break
        r = requests.get(req)
        data = r.json()
