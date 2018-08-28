#!/usr/bin/node
/*
returns the addition of two ints
*/
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
