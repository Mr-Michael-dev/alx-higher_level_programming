#!/usr/bin/node

/**
 * class Square that defines a square
 * inherits from Rectangle
 */

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
