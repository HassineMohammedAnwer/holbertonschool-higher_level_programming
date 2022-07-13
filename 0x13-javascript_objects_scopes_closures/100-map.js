#!/usr/bin/node
const l = require('./100-data').list;
console.log(l);
let i = 0;
const newl = l.map(x => x * i++);
console.log(newl);
