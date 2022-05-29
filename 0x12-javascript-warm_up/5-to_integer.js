#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('No argument');
} else {
  console.log('My number:', process.argv[2]);
}
