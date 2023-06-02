#!/usr/bin/node
// script that prints all characters of a Star Wars movie
const request = require('request');
const filmId = process.argv[2]; // Movie ID passed as a command line argument
const apiUrl = {
  url: 'https://swapi-api.alx-tools.com/api/films/' + filmId,
  method: 'GET'
};

// Make a GET request to retrieve the movie data
request(apiUrl, function (error, response, body) {
  if (!error) {
    // Extract the characters from the movie data
    const characters = JSON.parse(body).characters;
    printXterNames(characters, 0); // Start printing the character names
  }
});

// Recursive function to print the characters' names
function printXterNames (characters, index) {
  // Make a GET request for each character URL
  const characterUrl = characters[index];
  request(characterUrl, function (error, response, body) {
    if (!error) {
      // Extract the character's name from the response data
      const characterData = JSON.parse(body);
      console.log(characterData.name);
      // Check if there are more characters to print
      if (index + 1 < characters.length) {
        // Start printing recursively with the next character index
        printXterNames(characters, index + 1);
      }
    }
  });
}
