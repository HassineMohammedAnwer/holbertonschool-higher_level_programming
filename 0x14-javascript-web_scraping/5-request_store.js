#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const a1 = process.argv[2];
const a2 = process.argv[3];

request(a1, a2, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  fs.writeFile(a2, body, 'utf8', function (error) {
    if (error) {
      console.log(error);
    }
  });
});
