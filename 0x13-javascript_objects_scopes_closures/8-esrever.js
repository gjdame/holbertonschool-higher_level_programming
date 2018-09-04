#!/usr/bin/node
/*
reverses a list w/o builtin call reverse
*/
exports.esrever = function (list) {
  let result = [];

  for (let i = list.length - 1; i >= 0; i--) {
    result.push(list[i]);
  }

  return (result);
};
