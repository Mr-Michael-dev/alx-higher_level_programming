#!/usr/bin/node

const findSecondLargest = (args) => {
  const integers = args.map(arg => parseInt(arg, 10)).filter(Number.isInteger);

  if (integers.length < 2) {
    console.log(0);
  } else {
    const sortedIntegers = integers.sort((a, b) => b - a);
    console.log(sortedIntegers[1]);
  }
};

const argumentsList = process.argv.slice(2);
findSecondLargest(argumentsList);
