#!/usr/bin/node
/*
prints the number of arguments already printed
*/
exports.converter = function (base) {
  return function(num) {
    return num.toString(base);
  };
};
