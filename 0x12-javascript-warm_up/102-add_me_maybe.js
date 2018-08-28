#!/usr/bin/node
/*
returns the addition of two ints
*/
exports.addMeMaybe = function (number, theFunction) {
  let newNum = number + 1;
  theFunction(newNum);
};
