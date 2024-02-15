#!/usr/bin/node
const { argv } = require('node:process');

const num1 = Number(argv[2]), num2 = Number(argv[3]);

if (isNaN(num1) || isNaN(num2)) {
  console.log('NaN');
} else {
  console.log(num1 + num2);
}
