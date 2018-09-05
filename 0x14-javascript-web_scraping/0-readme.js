#!/usr/bin/node
/*
reads a file and prints the contents
*/
const fs = require('fs');

let file = process.argv[2];

fs.readFile(file, function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString());
  }
});
