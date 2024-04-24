#!/usr/bin/node

const { argv } = require('node:process');
const fs = require('fs');

const file = argv[2];

fs.readFile(file, 'utf8', (err, text) => {
  if (err) {
    console.log(err);
  }
  console.log(text);
});
