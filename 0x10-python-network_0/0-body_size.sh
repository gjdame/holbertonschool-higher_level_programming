#!/bin/bash
curl -sI $1 | grep 'Content-Length' | cut -f2 -d ':'
