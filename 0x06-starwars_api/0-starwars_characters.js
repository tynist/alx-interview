#!/usr/bin/node
// script that prints all characters of a Star Wars movie:

const request = require('request');

// Movie ID passed as a command line argument
const filmID = process.argv[2];

// API URL for the movie
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${filmID}`;

// Make a GET request to retrieve the movie data
request(apiUrl, function (error, response, body) {
  if (!error) {
    // Parse the movie data from the response
    const filmData = JSON.parse(body);
    // Array of character URLs from the movie data
    const characterUrls = filmData.characters;
    // Start printing character names recursively
    printXterNames(characterUrls, 0);
  }
});

// Recursive function to print the characters' names
function printXterNames(characterUrls, index) {
  if (index >= characterUrls.length) {
    return; // Base case: all characters have been printed
  }

  // URL of the current character
  const characterUrl = characterUrls[index];
  // Make a GET request for each character URL
  request(characterUrl, function (error, response, body) {
    if (!error) {
      // Parse the character data from the response
      const character = JSON.parse(body);
      console.log(character.name); // Print the character name
      // printXterNames function recursively with the next character index
      printXterNames(characterUrls, index + 1);
    }
  });
}
