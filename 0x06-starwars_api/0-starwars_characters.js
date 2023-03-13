#!/usr/bin/env node

const request = require('request');
const movieID = process.argv[2];
const api = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

const getFilmBody = () => {
  return new Promise((resolve, reject) => {
    request(api, { json: true }, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        resolve(body.characters);
      } else {
        reject(error);
      }
    });
  });
};

const getCharacterNames = (nameAPI) => {
  return new Promise((resolve, reject) => {
    request(nameAPI, { json: true }, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        resolve(body.name);
      } else {
        reject(error);
      }
    });
  });
};

getFilmBody()
  .then((characters) => {
    const promises = characters.map((character) => {
      return getCharacterNames(character);
    });

    Promise.all(promises)
      .then((names) => {
        for (const name of names) {
          process.stdout.write(name + '\n');
        }
      })
      .catch((error) => console.error(error));
  })
  .catch((error) => console.log(error));
