#!/usr/bin/node
/*
creates a square class that inherits from Rectangle
*/
const Rectangle = require('./5-square');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log((c.repeat(this.width)));
    }
  }
};
