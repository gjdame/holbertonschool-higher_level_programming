#!/bin/bash
# takes in a url and displays all http methods
curl -sI $1 | grep 'Allow' | cut -f2 -d ':'
