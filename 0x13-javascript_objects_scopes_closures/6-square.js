#!/usr/bin/node
const Squared = require('./5-square');

module.exports = class Square extends Squared {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    if (c && typeof c === 'string') {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    } else {
        this.print();
    }
  }
};
