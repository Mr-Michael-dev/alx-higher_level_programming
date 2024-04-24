#!/usr/bin/node
/**
 * prints the number of movies where the character “Wedge Antilles” is present
 */

const request = require('request');

// API URL provided as the first argument
const url = process.argv[2];

// Character ID for "Wedge Antilles"
const characterId = 18;

// Make a request to the API URL
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const filmsData = JSON.parse(body);
  let count = 0;

  // Loop through each film
  for (const film of filmsData) {
    // Check if the characters array includes Wedge Antilles
    for (const character of film.characters) {
      if (character === `https://swapi-api.alx-tools.com/api/people/${characterId}/`) {
        count++;
        break; // Exit the inner loop if the character is found
      }
    }
  }

  // Print the number of films
  console.log(count);
});
