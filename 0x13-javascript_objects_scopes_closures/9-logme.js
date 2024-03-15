#!/usr/bin/node

/**
 * prints the number of arguments already printed
 * and the new argument value
 *
 * Example: <number arguments already printed>: <current argument value>
 */

let logInstance = null;

exports.logMe = function (item) {
  class Logme {
    constructor () {
      this.logCount = 0;
    }

    printLog (item) {
      console.log(`${this.logCount}: ${item}`);
      this.logCount += 1;
    }
  }

  if (!logInstance) {
    logInstance = new Logme();
  }
  logInstance.printLog(item);
};
