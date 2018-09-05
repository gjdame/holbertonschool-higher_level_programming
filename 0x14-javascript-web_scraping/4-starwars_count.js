#!/usr/bin/node
/*
prints the title of a Star Wars movie
the episode number matches a given integer.
*/
const request = require('request');

let url = 'http://swapi.co/api/films/';
let count = 0;

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    let json = JSON.parse(body);
    let results = json.results;
    for (let i = 0; i < results.length; i++) {
      for (let j = 0; j < results[i]['characters'].length; j++) {
        let s = results[i]['characters'][j];
        if (s.includes('/18/')) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
