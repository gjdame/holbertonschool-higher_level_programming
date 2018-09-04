#!/usr/bin/node
/*
Function returns number of occurences in a list
*/
'use strict';
exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;

  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      occurences += 1;
    }
  }
  return (occurences);
};
