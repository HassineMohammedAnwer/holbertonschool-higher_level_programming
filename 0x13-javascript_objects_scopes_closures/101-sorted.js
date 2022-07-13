#!/usr/bin/node
const d = require('./101-data.js').dict;
const newd = {};
for (const key in d) {
  if (newd[d[key]] === undefined) {
    newd[d[key]] = [];
  }
  newd[d[key]].push(key);
}
console.log(newd);
