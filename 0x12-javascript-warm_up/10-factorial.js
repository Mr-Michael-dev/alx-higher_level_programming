#!/usr/bin/node

const { argv } = require('node:process');

function factorial(n) {
if (isNaN(n)) {
    return 1;
  } else if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

result = factorial(parseInt(argv[2]));

console.log(result);
