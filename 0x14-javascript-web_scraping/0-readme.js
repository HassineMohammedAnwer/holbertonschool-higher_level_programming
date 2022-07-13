#!/usr/bin/node

const fs = require('fs');

try {
  const f1 = process.argv[2];
  const data = fs.readFileSync(f1,
    { encoding: 'utf8', flag: 'r' });
  console.log(data);
} catch (err) {
  console.log(err);
}
