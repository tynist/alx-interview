#!/usr/bin/node
// script that prints all characters of a Star Wars movie:
const request = require('request');
const filmID = process.argv[2]; // Movie ID passed as a command line argument
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${filmID}`; // API URL for the movie

// Make a GET request to retrieve the movie data
request(apiUrl, function (error, response, body) {
  if (!error) {
    const filmData = JSON.parse(body); // Parse the movie data from the response
    const characterUrls = filmData.characters; // Array of character URLs from the movie data
    printCharacterNames(characterUrls, 0); // Start printing character names recursively
  }
});

// Recursive function to print the characters' names
function printCharacterNames(characterUrls, index) {
  if (index >= characterUrls.length) {
    return; // Base case: all characters have been printed
  }

  const characterUrl = characterUrls[index]; // URL of the current character
  // Make a GET request for each character URL
  request(characterUrl, function (error, response, body) {
    if (!error) {
      const character = JSON.parse(body); // Parse the character data from the response
      console.log(character.name); // Print the character name
      // Call the printCharacterNames function recursively with the next character index
      printCharacterNames(characterUrls, index + 1);
    }
  });
}
