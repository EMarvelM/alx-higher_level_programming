#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    if (size > 0) {
      super(constructor);
      this.width = this.height = size;
    }
  }
};
