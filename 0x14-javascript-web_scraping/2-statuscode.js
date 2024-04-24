#!/usr/bin/node
/**
 *  display the status code of a GET request
 *  Usage: ./2-statuscode.js <url>
 */

const request = require('request');
const args = process.argv;

request(args[2], (err, response) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('code:', response.statusCode);
});
