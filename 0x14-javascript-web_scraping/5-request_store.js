#!/usr/bin/node
/**
 * prints the number of movies where the character “Wedge Antilles” is present
 */

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

// Make a request to the API URL
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  // const filmsData = JSON.parse(body);

  fs.writeFile(file, body, (err) => {
    if (err) {
      console.error(err);
    }
  });
});
