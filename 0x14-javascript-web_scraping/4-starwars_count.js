#!/usr/bin/node
/**
 * prints the number of movies where the character “Wedge Antilles” is present
 */

const request = require('request');
const fs = require('fs')

// API URL provided as the first argument
const url = process.argv[2];
const file = process.argv[3];

// Character ID for "Wedge Antilles"
// const characterId = 18;

// Make a request to the API URL
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const filmsData = JSON.parse(body);

  fs.writeFile(file, JSON.stringify(filmsData), (err) => {
    if (err) {
      console.error(err);
    }
  });
  // console.log(filmsData[1]);
});
