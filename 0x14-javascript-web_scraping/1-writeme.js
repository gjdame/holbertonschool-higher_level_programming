#!/usr/bin/node
/*
reads a file and prints the contents
*/
const fs = require('fs');

let file = process.argv[2];
let content = process.argv[3];

fs.writeFile(file, content, function (err) {
  if (err) {
    console.log(err);
  }
});
