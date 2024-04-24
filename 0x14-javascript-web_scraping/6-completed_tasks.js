#!/usr/bin/node
/**
 * computes the number of tasks completed by user id
 */

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const tasks = JSON.parse(body);
  const completedTasksByUserId = {};
  for (const task of tasks) {
    if (task.completed) {
      const userId = task.userId;
      completedTasksByUserId[userId] = (completedTasksByUserId[userId] || 0) + 1;
    }
  }
  console.log(completedTasksByUserId);
});
