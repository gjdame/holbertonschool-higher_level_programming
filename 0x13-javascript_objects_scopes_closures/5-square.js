#!/usr/bin/node
/*
creates a square class that inherits from Rectangle
*/
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
