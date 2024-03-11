#!/usr/bin/node
const { argv } = require('node:process');

console.log(add(argv[2], argv[3]));

function add (a, b) {
  return Number(a) + Number(b);
}
