#!/usr/bin/node
const { argv } = require('node:process');

const myNumber = Number(argv[2]);

if (isNaN(myNumber) === false) {
  console.log('My number: ' + myNumber);
} else {
  console.log('Not a number');
}
