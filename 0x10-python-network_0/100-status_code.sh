#!/bin/bash
#returns status code
curl -o -I -L -s -w "%{http_code}" $1
