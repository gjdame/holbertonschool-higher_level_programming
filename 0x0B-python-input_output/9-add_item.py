#!/usr/bin/python3
import json
import sys
"""laods adds and saves a file"""

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

num = len(sys.argv)


try:
    data = load_from_json_file('add_item.json')
except:
    data = []

for i in range(1, num):
    data.append(sys.argv[i])
save_to_json_file(data, 'add_item.json')
