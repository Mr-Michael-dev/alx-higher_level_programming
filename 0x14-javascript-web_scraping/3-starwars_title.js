#!/usr/bin/node
/**
 * prints the title of a Star Wars movie
 * where the episode number matches a given integer
 *  Usage: ./3-starwars_title.js <episode number>
 */

const request = require('request');
const args = process.argv;

request('https://swapi-api.alx-tools.com/api/films/${args[2]}', (err, response,data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('code:', response.statusCode);
});
