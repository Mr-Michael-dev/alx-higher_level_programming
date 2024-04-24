#!/usr/bin/node
/**
 *  reads and prints the content of a file
 *  Usage: ./0-readme.js <path/to/file>
 */

const fs = require('fs');
const args = process.argv;

fs.readFile(args[2], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
