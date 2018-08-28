#!/usr/bin/node
/*
prints statements about c, python, and javascript */
'use strict';
if ((process.argv[2]) === undefined) {
  console.log('No Argument');
} else {
  console.log(process.argv[2]);
}
