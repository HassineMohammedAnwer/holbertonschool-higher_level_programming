#!/usr/bin/node
// Include fs module
const fs = require('fs');
const f1 = process.argv[2];
const f2 = process.argv[3];
const f3 = process.argv[4];
const data1 = fs.readFileSync(f1,
  { encoding: 'utf8', flag: 'r' });
const data2 = fs.readFileSync(f2,
  { encoding: 'utf8', flag: 'r' });
fs.writeFileSync(f3, data1 + data2);
