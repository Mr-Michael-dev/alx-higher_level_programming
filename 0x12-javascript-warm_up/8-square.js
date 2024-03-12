#!/usr/bin/node

const { argv } = require('node:process');
const number = parseInt(argv[2], 10);

if (isNaN(number)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < number) {
    let j = 0;
    while (j < number) {
      process.stdout.write('X');
      j++;
    }
    console.log();
    i++;
  }
}
