#!/usr/bin/node
/*
reads a file and prints the contents
*/
const fs = require('fs');

file = process.argv[2];

fs.readFile(file, function(err, data) {
  if (err) {
    throw err;
  }
  console.log(data.toString());
});
