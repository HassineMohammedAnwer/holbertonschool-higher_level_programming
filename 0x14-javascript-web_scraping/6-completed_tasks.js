#!/usr/bin/node

const request = require('request');
const a1 = process.argv[2];
request.get(a1, function (error, response, body) {
  if (!error) {
    const tar = JSON.parse(body);
    const ctar = {};
    for (const i of tar) {
      if (i.ctar === true) {
        if (i.userId in ctar) {
          ctar[i.userId] += 1;
        } else {
          ctar[i.userId] = 1;
        }
      }
    }
    console.log(ctar);
  }
});
