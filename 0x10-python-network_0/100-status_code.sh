#!/bin/bash
#returns status code
curl -sI $1 | grep HTTP | cut -d ' ' -f2
