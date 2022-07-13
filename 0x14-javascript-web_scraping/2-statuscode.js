#!/usr/bin/node
const axios = require('axios');

// Make a request
axios.get(process.argv[2])
  .then(function (response) {
// handle success
    console.log('code:', response.status);
});
