#!/usr/bin/python3
'''get commits from user rails'''
import sys
import requests

if __name__ == "__main__":
    user = sys.argv[2]
    repo = sys.argv[1]
    req = "https://api.github.com/repos/" + user + '/' + repo + '/commits'
    r = requests.get(req)
    data = r.json()
    count = 0
    for dic in data:
        print("{}: {}".format(dic.get('sha'),
                              dic.get('commit').get('author').get('name')))
        count += 1
        if count == 10:
            break
