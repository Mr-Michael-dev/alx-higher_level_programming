#!/usr/bin/node
/**
 * prints the number of movies where the character “Wedge Antilles” is present
 */

const request = require('request');
const filmId = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${filmId}/`, (err, response, body) => {
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

  const characters = filmsData.characters;

  for (const character of characters) {
    request(character, (err, response, body) => {
      if (err) {
        console.error(err);
        return;
      }
      const characterName = JSON.parse(body);
      console.log(characterName.name);
    });
  }
});
