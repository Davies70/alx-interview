#!/usr/bin/node

const request = require("request");
const api = `https://swapi-api.alx-tools.com/api/films/3`;

const getFilmBody = () => {
  return new Promise((resolve, reject) => {
    request(api, { json: true }, (error, response, body) => {
      if (!error && response.statusCode == 200) {
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
      if (!error && response.statusCode == 200) {
        resolve(body.name);
      } else {
        reject(error);
      }
    });
  });
};

getFilmBody().then((characters) => {
  const promises = characters.map((character) => {
    return getCharacterNames(character);
  });

  Promise.all(promises)
    .then((names) => {
      names.map((actorName) => console.log(actorName));
    })
    .catch((error) => console.error(error));
});
