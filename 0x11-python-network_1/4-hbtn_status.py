#!/usr/bin/python3
'''fetches status of https://intranet.hbtn.io/status'''
import requests

r = requests.get('https://intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(type(r.text)))
print("\t- content: {}".format(r.text))
