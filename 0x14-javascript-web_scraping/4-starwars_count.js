#!/usr/bin/node
/**
 * prints the number of movies where the character “Wedge Antilles” is present
 */

const request = require('request');
const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  let filmsData;
  try {
    filmsData = JSON.parse(body);
  } catch (error) {
    console.error('Error parsing JSON:', error);
    return;
  }

  let count = 0;

  const films = filmsData.results;

  for (const film of films) {
    // Check if the characters array includes Wedge Antilles
    for (const character of film.characters) {
      if (character === `https://swapi-api.alx-tools.com/api/people/${characterId}/`) {
        count++;
        break;
      }
    }
  }

  console.log(count);
});
