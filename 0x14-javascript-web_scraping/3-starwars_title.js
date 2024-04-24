#!/usr/bin/node
/**
 * prints the title of a Star Wars movie
 * where the episode number matches a given integer
 * Usage: ./3-starwars_title.js <episode number>
 */

const request = require('request');
const args = process.argv;
const episodeNumber = parseInt(args[2]);

request(`https://swapi-api.alx-tools.com/api/films/${episodeNumber}`, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const data = JSON.parse(body);
  console.log(data.title);
});
