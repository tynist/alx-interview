#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Movie ID is required as an argument.');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }
  
  if (response.statusCode !== 200) {
    console.error('Failed to retrieve movie data:', response.statusCode);
    process.exit(1);
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  characters.forEach(function (characterUrl) {
    request(characterUrl, function (error, response, body) {
      if (error) {
        console.error('Error:', error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error('Failed to retrieve character data:', response.statusCode);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
