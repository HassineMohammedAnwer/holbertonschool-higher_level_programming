#!/usr/bin/node

const fs = require('fs');

const f1 = process.argv[2];
const data = process.argv[3];
fs.writeFileSync(f1, data);
