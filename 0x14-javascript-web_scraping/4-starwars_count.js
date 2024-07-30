#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const wedgeAntillesId = 'https://swapi-api.alx-tools.com/api/people/18/';

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;

    films.forEach(film => {
      if (film.characters.includes(wedgeAntillesId)) {
        count++;
      }
    });

    console.log(count);
  } else {
    console.error('Error:', error || `Status code: ${response.statusCode}`);
  }
});
