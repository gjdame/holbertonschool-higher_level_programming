#!/usr/bin/node
/*
prints the number of arguments already printed
*/
let count = 0;

exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count += 1;
};
