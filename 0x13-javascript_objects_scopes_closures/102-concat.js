#!/usr/bin/node
//const fs = require('fs');
const f1 =process.argv[2];
const f2 =process.argv[3];
const f3 =process.argv[4];


//fs.writeFileSync(f3, contents + contents2);

var fs = require('fs');
fs.readFile(f1, 'utf8', (err, data) => {
});
var fs = require('fs');
fs.readFile(f2, 'utf8', (err, data2) => {
});
fs.writeFileSync(f3, data + data2);
