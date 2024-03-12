#!/usr/bin/node
module.export = class Rectangle {
  constructor (w, h) {
    if (w < 1 || h < 1) {
      this.widht = w;
      this.height =h;
    }
  }
}
