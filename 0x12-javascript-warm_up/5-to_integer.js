#!/usr/bin/node
/*
prints statements about c, python, and javascript */
'use strict';
const arg1 = process.argv[2];
const integer = parseInt(arg1, 10);
if (isNaN(integer)) {
  console.log('Not a number');
} else {
  console.log('My number:', integer);
}
