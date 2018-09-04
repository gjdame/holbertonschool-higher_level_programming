#!/usr/bin/node
/*
set up rectangle class
*/
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    let newWidth = this.height;
    let newHeight = this.width;
    this.width = newWidth;
    this.height = newHeight;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
