#!/usr/bin/node

const myVar = 'X';
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 1; i <= process.argv[2]; i++) {
    console.log(myVar.repeat(process.argv[2]));
  }
}
