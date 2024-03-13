#!/usr/bin/node

/**
 * returns the reversed version of a list
 */

exports.esrever = function (list) {
  const reversedList = [];
  const length = list.length - 1;
  for (let i = 0; i <= length; i++) {
    reversedList.push(list[length - i]);
  }

  return reversedList;
};
