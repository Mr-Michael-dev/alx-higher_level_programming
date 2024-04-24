#!/usr/bin/node
/**
 * Prints all characters of a Star Wars movie in the same order as the list “characters” in the /films/ response.
 */

const request = require('request-promise');
const filmId = process.argv[2];

(async () => {
  try {
    // Make request to fetch film data
    const filmData = await request(`https://swapi-api.alx-tools.com/api/films/${filmId}/`, { json: true });
    const characters = filmData.characters;

    // Sequentially fetch character data and print names
    for (const characterUrl of characters) {
      const characterData = await request(characterUrl, { json: true });
      console.log(characterData.name);
    }
  } catch (error) {
    console.error('Error:', error);
  }
})();
