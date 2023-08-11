#!/usr/bin/node
// Anakin SkyWalker
// STAR WARS ! THE CLONE WARS
// I need a life, lol
const request = require('request');
const id = process.argv[2];
const starWarsApi = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(starWarsApi, async function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const getResults = JSON.parse(body);
    for (const results of getResults.characters) {
      await new Promise((resolve, reject) => {
        request(results, function (err, res, body2) {
          if (res) {
            const charactersName = JSON.parse(body2);
            console.log(charactersName.name);
            resolve();
          } else {
            console.log(err);
          }
        });
      });
    }
  }
});
