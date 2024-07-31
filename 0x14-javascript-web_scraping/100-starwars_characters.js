#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

if (!movieId) {
  console.error('Usage: ./100-starwars_characters.js <Movie-ID>');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Error: Status code', response.statusCode);
    process.exit(1);
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;

  characters.forEach(character => {
    request(character, (charError, charResponse, charBody) => {
      if (charError) {
        console.error(charError);
        return;
      }

      if (charResponse.statusCode !== 200) {
        console.error('Error: Status code', charResponse.statusCode);
        return;
      }

      const characterDetails = JSON.parse(charBody);
      console.log(characterDetails.name);
    });
  });
});
