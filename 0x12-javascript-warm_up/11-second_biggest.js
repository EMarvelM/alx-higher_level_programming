#!/usr/bin/node
const { argv } = require('node:process');
numbers = [];
argv.forEach( (num) => numbers.push(Number(num)));

if (argv[2]) {
    console.log(numbers.splice(2).sort((a, b) => a - b).slice(-2)[0]);
  } else if (!isNaN(Number(numbers[2]))) {
    console.log(0);
  }