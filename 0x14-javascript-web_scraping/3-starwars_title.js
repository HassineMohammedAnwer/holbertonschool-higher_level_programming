#!/usr/bin/node

const request = require('request');
const ap = 'https://swapi-api.hbtn.io/api/films/';

request.get(ap + process.argv[2], function (error, response, body) {
  console.log(JSON.parse(body).title);
});
