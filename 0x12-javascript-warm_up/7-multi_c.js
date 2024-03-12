#!/usr/bin/node

const { argv } = require('node:process');
const number = parseInt(argv[2], 10)

if (isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < number) {
  console.log('C is fun');
  i++;
  }
}
