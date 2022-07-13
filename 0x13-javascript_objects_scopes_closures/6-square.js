#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    const size = this.height;
    for (let i = 0; i < size; i++) {
      for (let j = 0; j < size; j++) {
        process.stdout.write(c);
      }
      console.log();
    }
  }
};
