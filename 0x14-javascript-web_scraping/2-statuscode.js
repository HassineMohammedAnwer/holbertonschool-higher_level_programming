#!/usr/bin/node
const axios = require('axios').default;

axios.get(process.argv[2])
  .then(response => {
    // Handle response
    console.log('code:', response.status);
  })
