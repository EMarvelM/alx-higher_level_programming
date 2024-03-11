#!/usr/bin/node
const { argv } = require('node:process');
if (argv[2]) {
  if (!isNaN(Number(argv[2]))) {
    console.log('\nC is fun'.repeat(Number(argv[2])).replace(/\n/, ''));
  }
} else {
  console.log('Missing number of occurrences');
}