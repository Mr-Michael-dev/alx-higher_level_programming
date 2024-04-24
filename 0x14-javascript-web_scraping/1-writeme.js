#!/usr/bin/node
/**
 *  writes a string to a file
 *  Usage: ./1-writeme.js <path/to/file> <content/string to write>
 */

const fs = require('fs');
const args = process.argv;

fs.writeFile(args[2], args[3], (err) => {
  if (err) {
    console.error(err);
  }
});
