#!/usr/bin/node
const axios = require('axios').default;
const request = require('request');
axios.get(process.argv[2])
  .then(response => {
  })
const argv = process.argv;
request.get(argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
