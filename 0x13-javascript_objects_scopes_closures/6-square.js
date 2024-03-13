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

  charPrint (c) {
    /**
     * Instance method
     * prints the rectangle using c or X if c is undefined
     */

    for (let i = 0; i < this.height; i++) {                 let row = '';                                         for (let j = 0; j < this.width; j++) {
        if (c === undefined) {
          row += 'X';
	} else {
	    row += c;
	}
      }                                                     console.log(row);
    }
  }
}

module.exports = Square;
