#!/usr/bin/node
const { argv } = require('node:process');

const num = Number(argv[2]);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let block = '';
    for (let j = 0; j < num; j++) {
      block += 'x';
    }
    console.log(block);
  }
}
