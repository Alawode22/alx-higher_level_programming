#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request(apiUrl, (error, response, body) => {
  const film = JSON.parse(body);
  console.log(film.title);
});
