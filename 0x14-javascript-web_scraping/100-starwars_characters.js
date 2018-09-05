#!/usr/bin/node
/*
prints the title of a Star Wars movie
the episode number matches a given integer.
*/
const request = require('request');

let url = 'http://swapi.co/api/films/' + process.argv[2];

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    let results = JSON.parse(body);
    let characters = results['characters'];
    for (let j = 0; j < characters.length; j++) {
      let peopleUrl = characters[j];
      request(peopleUrl, function (err, res, body) {
        if (err) {
          console.log(err);
        } else {
          let person = JSON.parse(body);
          console.log(person.name);
        }
      });
    }
  }
});
