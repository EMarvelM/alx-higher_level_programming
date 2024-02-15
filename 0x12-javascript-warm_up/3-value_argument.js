#!/usr/bin/node

const { argv } = require('node:process');

if (argv[2] == null) {
  console.log('No argument');
} else if (argv[2] != 'undefined') {
  console.log(process.argv[2]);
}
