#!/usr/bin/node

/**
 * class Rectangle that defines a rectangle
 */

class Rectangle {
  /**
   * Rectangle Class
   */
  constructor (w, h) {
    if (w <= 0 || w === undefined || h <= 0 || h === undefined) {
      return this;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    /**
     * Instance method
     * prints the rectangle using X
     */

    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}

module.exports = Rectangle;
