#!/usr/bin/node
/*
prints the title of a Star Wars movie
the episode number matches a given integer.
*/
const request = require('request');

let id = process.argv[2];
let url = 'http://swapi.co/api/films/' + id;

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    let json = JSON.parse(body);
    console.log(json.title);
  }
});
