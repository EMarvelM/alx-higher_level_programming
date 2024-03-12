#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(constructor);
    if (size > 0) {
      this.width = this.height = size;
    }
  }
};
