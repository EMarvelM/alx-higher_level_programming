#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        let x = '';
        for (let j = 0; j < this.width; j++) {
          x += 'x';
        }
        console.log(x);
      }
    }
  }

  rotate () {
    if (this.width && this.height) {
      const temp = this.height;
      this.height = this.width;
      this.width = temp;
    }
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
